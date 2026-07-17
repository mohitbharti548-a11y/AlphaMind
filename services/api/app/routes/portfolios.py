from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, Depends, status
from app.auth.dependencies import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.portfolio import (
    PortfolioCreate,
    PortfolioResponse,
    PortfolioUpdate,
)
from app.services.portfolio_service import (
    create_portfolio,
    get_portfolios,
    get_portfolio,
    update_portfolio,
    delete_portfolio,
)

router = APIRouter(
    prefix="/portfolios",
    tags=["Portfolios"],
)


@router.post(
    "/",
    response_model=PortfolioResponse,
)
def create_new_portfolio(
    portfolio: PortfolioCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_portfolio(
        db=db,
        name=portfolio.name,
        user_id=current_user.id,
    )


@router.get(
    "/",
    response_model=list[PortfolioResponse],
)
def list_my_portfolios(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_portfolios(
        db=db,
        user_id=current_user.id,
    )

@router.get(
    "/{portfolio_id}",
    response_model=PortfolioResponse,
)
def get_one_portfolio(
    portfolio_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    portfolio = get_portfolio(
        db,
        portfolio_id,
        current_user.id,
    )

    if not portfolio:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return portfolio


@router.put(
    "/{portfolio_id}",
    response_model=PortfolioResponse,
)
def edit_portfolio(
    portfolio_id: int,
    data: PortfolioUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    portfolio = get_portfolio(
        db,
        portfolio_id,
        current_user.id,
    )

    if not portfolio:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    return update_portfolio(
        db,
        portfolio,
        data.name,
    )


@router.delete("/{portfolio_id}")
def remove_portfolio(
    portfolio_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    portfolio = get_portfolio(
        db,
        portfolio_id,
        current_user.id,
    )

    if not portfolio:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    delete_portfolio(
        db,
        portfolio,
    )

    return {
        "message": "Portfolio deleted successfully"
    }