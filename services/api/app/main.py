from fastapi import FastAPI
from app.core.config import settings
from app.db.database import engine
from app.db.base import Base
from app.routes import users
from app.routes.auth import router as auth_router
from app.routes import portfolios
from app.routes.transactions import router as transaction_router
from app.routes.analytics import router as analytics_router
from app.routes.dashboard import router as dashboard_router
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI Financial Intelligence Platform",
)
app.include_router(dashboard_router)
app.include_router(auth_router)
app.include_router(users.router)
app.include_router(portfolios.router)
app.include_router(transaction_router)
app.include_router(analytics_router)
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