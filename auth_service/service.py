import json
import logging

from fastapi import HTTPException
from starlette import status

from schemas import RegisterSchema, LoginSchema, JWTSchema
from httpx import AsyncClient, Response, HTTPStatusError
from config import MONGO_SERVICE_V1_URL
from utils import hash_password, verify_password, create_jwt_token


logger = logging.getLogger(__name__)

class UserManager:
    @staticmethod
    async def register_user(register_data: RegisterSchema):
        async with AsyncClient() as client:
            try:
                register_data.password = hash_password(register_data.password)
                result: Response = await client.post(
                    url=f"{MONGO_SERVICE_V1_URL}/register",
                    json=register_data.dict()
                )
                result.raise_for_status()
                logger.info(f'User: {register_data.username} has been successfully registered')
                return result.json()
            except HTTPStatusError as exc:
                raise HTTPException(status_code=exc.response.status_code,
                                    detail=json.loads(exc.response.text).get('detail') if exc.response.text else str(exc))

    @staticmethod
    async def authorization(auth_data: LoginSchema) -> JWTSchema:
        async with AsyncClient() as client:
            try:
                exist_user = await client.post(
                    url=f"{MONGO_SERVICE_V1_URL}/find",
                    json=auth_data.username
                )
                exist_user.raise_for_status()
                check_password = verify_password(exist_user.json().get('password'), auth_data.password)
                if not check_password:
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Incorrect password!')
                jwt_token = create_jwt_token(auth_data)
                return jwt_token
            except HTTPStatusError as exc:
                raise HTTPException(status_code=exc.response.status_code,
                                    detail=json.loads(exc.response.text).get('detail') if exc.response.text else str(exc))
