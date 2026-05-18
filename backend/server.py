"""Ess Bee Heaters API entry point - slim assembly of modular routers."""
import logging
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from database import client, UPLOAD_DIR
from seed import seed_if_empty
from auth import router as auth_router
from routes.public_routes import router as public_router
from routes.admin_routes import router as admin_router

app = FastAPI(title="Ess Bee Heaters API")

# All API routes live under /api
api_router = APIRouter(prefix="/api")
api_router.include_router(public_router)
api_router.include_router(auth_router)
api_router.include_router(admin_router)
app.include_router(api_router)

# Serve uploaded images
app.mount("/api/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def on_startup():
    await seed_if_empty()


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
