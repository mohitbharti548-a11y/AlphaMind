from fastapi import FastAPI
from app.core.config import settings
from app.db.database import engine
from app.db.base import Base
from app.routes.auth import router as auth_router
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI Financial Intelligence Platform",
)
Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
@app.get("/")
async def root():
    return {
        "project": "AlphaMind",
        "version": "1.0.0",
        "status": "Running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }