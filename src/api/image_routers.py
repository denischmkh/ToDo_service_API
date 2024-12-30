from uuid import UUID
import uuid

from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException
from starlette import status
import re



class RegisterSchema(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    username: str = Field(min_length=5, max_length=20)
    password1: str = Field(max_length=8)
    password2: str = Field(max_length=8)
    @model_validator(mode="before")
    @classmethod
    def validate_passwords(cls, values: dict) -> dict:
        password1 = values.get("password1")
        password2 = values.get("password2")
        if password1 != password2:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Second password')

        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", password1):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Password must contain:\n"
                "- At least one uppercase letter\n"
                "- At least one lowercase letter\n"
                "- At least one digit"
            )

        return values

