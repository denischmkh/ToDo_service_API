import logging

import uvicorn
from fastapi import FastAPI, APIRouter
from routers import router as router

app = FastAPI(debug=False)

routers = APIRouter(prefix='/api')
routers.include_router(router)

if __name__ == '__main__':
    app.include_router(routers)
    uvicorn.run(app,
                host='localhost',
                port=8000,
                log_level=logging.DEBUG,
                )
