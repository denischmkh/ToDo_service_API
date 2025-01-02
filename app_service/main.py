from fastapi import FastAPI, APIRouter

from routers import router_v1

app = FastAPI(title='API Service to render images',
              version='0.1.0')



app.include_router(router_v1)