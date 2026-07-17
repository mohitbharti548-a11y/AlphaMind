from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.services.analytics_service import calculate_holdings

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/{portfolio_id}")
def portfolio_summary(
    portfolio_id: int,
    db: Session = Depends(get_db),
):
    return calculate_holdings(
        db,
        portfolio_id,
    )