import os

from dotenv import load_dotenv

load_dotenv()


class DeveloperConfig:
    SQLALCHEMY_URL: str = 'postgresql+asyncpg://postgres:denis2004@localhost:5432/devdb'
    MONGO_CONNECT: str = ''
    PASSWORD_ENCRYPT_TOKEN: str = 'TestToken'
    JWT_TOKEN_SECRET: str = 'TestToken'
    S3_ACCESS_TOKEN: str = ''
    S3_SECRET_KEY: str = ''
    S3_ENDPOINT_URL: str = ''
    S3_BUCKET_NAME: str = ''


class ProdConfig:
    SQLALCHEMY_URL: str = os.getenv('SQLALCHEMY_URL')
    MONGO_CONNECT: str = os.getenv('MONGO_CONNECT')
    PASSWORD_ENCRYPT_TOKEN: str = os.getenv('PASSWORD_ENCRYPT_TOKEN')
    JWT_TOKEN_SECRET: str = os.getenv('JWT_TOKEN_SECRET')
    S3_ACCESS_TOKEN: str = os.getenv('S3_ACCESS_TOKEN')
    S3_SECRET_KEY: str = os.getenv('S3_SECRET_KEY')
    S3_ENDPOINT_URL: str = os.getenv('S3_ENDPOINT_URL')
    S3_BUCKET_NAME: str = os.getenv('S3_BUCKET_NAME')


class Config:
    def __init__(self):
        from src.main import DEBUG as debug_mode
        if debug_mode:
            self.config = DeveloperConfig()
        else:
            self.config = ProdConfig()

config = Config()
