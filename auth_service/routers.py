from typing import Annotated

from fastapi import APIRouter, Body
from schemas import RegisterSchema
from service import UserManager

router_v1 = APIRouter(prefix='/v1', tags=['Authentication API'])


@router_v1.post('/register')
async def register(register_data: Annotated[RegisterSchema, Body(...)]):
    response = UserManager.register_user(register_data=register_data)
