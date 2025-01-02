from schemas import RegisterSchema
from httpx import AsyncClient
from config import APP_SERVICE_V1_URL, MONGO_SERVICE_V1_URL


class UserManager:
    @staticmethod
    async def register_user(register_data: RegisterSchema):
        async with AsyncClient() as client:
            result = await client.post(
                url=f"{MONGO_SERVICE_V1_URL}/register",
                data=register_data.dict()
            )
            return result
