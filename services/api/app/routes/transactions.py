from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.services.portfolio_service import get_portfolio_by_id

from app.db.dependencies import get_db
from app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
)
from app.services.transaction_service import (
    create_transaction,
    get_transaction,
    get_transactions,
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post(
    "/",
    response_model=TransactionResponse,
)
def create(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    portfolio = get_portfolio_by_id(
        db,
        transaction.portfolio_id,
    )

    if portfolio is None:
        raise HTTPException(
            status_code=404,
            detail="Portfolio not found",
        )

    if portfolio.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed",
        )

    return create_transaction(db, transaction)


@router.get(
    "/",
    response_model=list[TransactionResponse],
)
def read_all(
    db: Session = Depends(get_db),
):
    return get_transactions(db)


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse,
)
def read_one(
    transaction_id: int,
    db: Session = Depends(get_db),
):
    transaction = get_transaction(
        db,
        transaction_id,
    )

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return transaction