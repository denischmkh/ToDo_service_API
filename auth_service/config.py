import os

from dotenv import load_dotenv

load_dotenv()

APP_SERVICE_V1_URL = os.getenv('APP_SERVICE_URL')
MONGO_SERVICE_V1_URL = os.getenv('MONGO_SERVICE_URL')