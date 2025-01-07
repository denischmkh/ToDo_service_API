from typing import Annotated

from fastapi import APIRouter, Body, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from service import MongoManager
from schemas import RegisterSchema

router_v1 = APIRouter(prefix='/v1', tags=['MongoDB API'])


@router_v1.post('/find')
async def authenticate_user(username: Annotated[str, Body(...)]):
    result = await MongoManager.find(username)
    if result:
        result.update({'_id': str(result.get('_id'))})
        return result
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not found!")

@router_v1.post('/register')
async def register_user(register_data: Annotated[RegisterSchema, Body(...)]):
    await MongoManager.register_user(register_data)
    return JSONResponse(status_code=200, content={'message': 'User successfully registered'})