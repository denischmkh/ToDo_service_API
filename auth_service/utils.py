from passlib.context import CryptContext

from schemas import LoginSchema, JWTSchema
from jose import jwt
from config import JWT_SECRET_KEY
import datetime



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(payload: str, password: str) -> bool:
    return pwd_context.verify(password, payload)


def create_jwt_token(user_data: LoginSchema) -> JWTSchema:
    payload = user_data.dict()
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload.update({'exp': expire})
    token = jwt.encode(claims=payload,
                       key=JWT_SECRET_KEY,
                       algorithm='HS256')
    token_schema = JWTSchema(token=token,
                             expire=expire.isoformat())
    return token_schema



