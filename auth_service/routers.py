import logging
from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from schemas import RegisterSchema, LoginSchema, JWTSchema
from service import UserManager

router_v1 = APIRouter(prefix='/v1', tags=['Authentication API'])

logger = logging.getLogger(__name__)


@router_v1.post('/register')
async def register(register_data: Annotated[RegisterSchema, Body(...)]):
    try:
        response = await UserManager.register_user(register_data=register_data)
        return response
    except HTTPException as http_exc:
        logger.error(f"HTTP Exception: {http_exc.detail}", exc_info=True)
    except Exception as exc:
        logger.critical("An unexpected error occurred", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router_v1.post('/login')
async def login(auth_data: Annotated[LoginSchema, Body(...)]):
    try:
        authorize_token: JWTSchema = await UserManager.authorization(auth_data)
        return authorize_token
    except HTTPException as http_exc:
        logger.error(f"HTTP Exception: {http_exc.detail}", exc_info=True)
    except Exception as exc:
        logger.critical("An unexpected error occurred", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")