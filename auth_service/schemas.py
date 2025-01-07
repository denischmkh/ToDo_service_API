import datetime

from pydantic import BaseModel, Field, model_validator
from fastapi.exceptions import HTTPException
from starlette import status


class RegisterSchema(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=8)
    confirm_password: str = Field(...)

    @model_validator(mode='before')
    def validate_passwords(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')

        # Проверка совпадения паролей
        try:
            if password != confirm_password:
                raise ValueError("Passwords do not match")

            # Проверка сложности пароля
            if not any(char.islower() for char in password):
                raise ValueError("Password must contain at least one lowercase letter")
            if not any(char.isupper() for char in password):
                raise ValueError("Password must contain at least one uppercase letter")
            if not any(char.isdigit() for char in password):
                raise ValueError("Password must contain at least one digit")
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.args)

        return values


class LoginSchema(BaseModel):
    username: str
    password: str


class JWTSchema(BaseModel):
    token: str
    expire: datetime.datetime
