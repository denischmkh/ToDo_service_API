import os

from dotenv import load_dotenv

load_dotenv()

MONGO_SERVICE_V1_URL = os.getenv('MONGO_SERVICE_URL')

JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')