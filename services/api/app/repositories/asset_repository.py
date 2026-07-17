from sqlalchemy.orm import Session

from app.models.asset import Asset


class AssetRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, asset: Asset):
        self.db.add(asset)
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def get_by_portfolio(self, portfolio_id: int):
        return (
            self.db.query(Asset)
            .filter(
                Asset.portfolio_id == portfolio_id
            )
            .all()
        )