from pydantic import BaseModel, Field, model_validator

from utils import pwd_context, hash_password


class RegisterSchema(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    password: str = Field(min_length=8, pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).*$")
    confirm_password: str = Field(alias='confirmPassword', exclude=True)
    @model_validator(mode='before')
    def compare_passwords(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if password != confirm_password:
            raise ValueError("Passwords do not match")
        values['password'] = hash_password(password)
        return values

