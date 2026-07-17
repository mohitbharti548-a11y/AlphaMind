from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.dashboard import DashboardSummary
from app.services.dashboard_service import get_dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/{portfolio_id}",
    response_model=DashboardSummary,
)
def dashboard(
    portfolio_id: int,
    db: Session = Depends(get_db),
):
    return get_dashboard(
        db,
        portfolio_id,
    )