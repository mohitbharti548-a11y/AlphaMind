from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class TransactionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, transaction: Transaction):
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_by_portfolio(self, portfolio_id: int):
        return (
            self.db.query(Transaction)
            .filter(
                Transaction.portfolio_id == portfolio_id
            )
            .all()
        )