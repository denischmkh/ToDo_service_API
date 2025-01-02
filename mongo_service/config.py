import os

from dotenv import load_dotenv

load_dotenv()

MONGO_CONNECT = os.getenv('MONGO_CONNECT')