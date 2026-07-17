from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.transaction import Transaction


def create_transaction(db: Session, transaction):
    db_transaction = Transaction(
        symbol=transaction.symbol,
        asset_name=transaction.asset_name,
        asset_type=transaction.asset_type,
        transaction_type=transaction.transaction_type,
        quantity=transaction.quantity,
        price=transaction.price,
        fees=transaction.fees,
        portfolio_id=transaction.portfolio_id,
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction


def get_transactions(db: Session):
    return db.query(Transaction).all()


def get_transaction(db: Session, transaction_id: int):
    return (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

def get_total_investment(
    db: Session,
    portfolio_id: int,
):
    total = (
        db.query(
            func.sum(
                Transaction.quantity *
                Transaction.price
            )
        )
        .filter(
            Transaction.portfolio_id == portfolio_id,
            Transaction.transaction_type == "BUY",
        )
        .scalar()
    )

    return total or 0