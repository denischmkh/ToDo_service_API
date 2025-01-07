import logging

from fastapi import FastAPI

from logging_config import setup_logging
from routers import router_v1

app = FastAPI(title='API Service to work with users',
              version='0.1.0')

logger = logging.getLogger(__name__)

@app.on_event('startup')
async def on_startup():
    setup_logging()
    logger.info('Auth service has been started!')

app.include_router(router_v1)
