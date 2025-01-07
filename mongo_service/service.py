from contextlib import asynccontextmanager
from pymongo.collection import Collection
import motor.motor_asyncio
from config import MONGO_CONNECT
from fastapi import HTTPException
from starlette import status

from schemas import RegisterSchema

@asynccontextmanager
async def get_client_collection() -> Collection:
    client = motor.motor_asyncio.AsyncIOMotorClient(
        MONGO_CONNECT
    )

    collection: Collection = client.Users.users

    try:
        yield collection
    finally:
        client.close()


class MongoManager:

    @staticmethod
    async def find(username) -> dict | None:
        async with get_client_collection() as collection:
            existing_user = await collection.find_one({'username': username})
            return existing_user

    @staticmethod
    async def register_user(register_data: RegisterSchema):
        async with get_client_collection() as collection:
            existing_user = await collection.find_one({'username': register_data.username})
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    detail='User already exists!'
                )
            await collection.insert_one(register_data.dict())
            return {"message": "User successfully registered"}
