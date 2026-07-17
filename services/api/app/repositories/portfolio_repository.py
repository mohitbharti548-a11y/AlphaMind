from sqlalchemy.orm import Session

from app.models.portfolio import Portfolio


class PortfolioRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, portfolio_id: int):
        return (
            self.db.query(Portfolio)
            .filter(Portfolio.id == portfolio_id)
            .first()
        )

    def get_by_user(self, user_id: int):
        return (
            self.db.query(Portfolio)
            .filter(Portfolio.user_id == user_id)
            .all()
        )

    def create(self, portfolio: Portfolio):
        self.db.add(portfolio)
        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio