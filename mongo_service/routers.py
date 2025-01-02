from typing import Annotated

from fastapi import APIRouter, Body

from schemas import UserSchema

router_v1 = APIRouter(prefix='/v1', tags=['MongoDB API'])


@router_v1.post('/register')
async def register_user(body: Annotated[UserSchema, Body()]):
    pass