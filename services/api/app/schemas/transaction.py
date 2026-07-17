from datetime import datetime

from pydantic import BaseModel

from app.core.enums import AssetType, TransactionType


class TransactionCreate(BaseModel):
    symbol: str
    asset_name: str
    asset_type: AssetType
    transaction_type: TransactionType
    quantity: float
    price: float
    fees: float = 0
    portfolio_id: int


class TransactionResponse(BaseModel):
    id: int
    symbol: str
    asset_name: str
    asset_type: AssetType
    transaction_type: TransactionType
    quantity: float
    price: float
    fees: float
    portfolio_id: int
    transaction_date: datetime

    model_config = {
        "from_attributes": True
    }