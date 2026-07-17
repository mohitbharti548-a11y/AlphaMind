from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.core.enums import TransactionType
from app.services.market_service import get_current_price


def calculate_holdings(db: Session, portfolio_id: int):
    transactions = (
        db.query(Transaction)
        .filter(Transaction.portfolio_id == portfolio_id)
        .all()
    )

    holdings = {}

    for tx in transactions:
        if tx.symbol not in holdings:
            holdings[tx.symbol] = {
                "symbol": tx.symbol,
                "asset_name": tx.asset_name,
                "quantity": 0,
                "invested": 0,
            }

        if tx.transaction_type == TransactionType.BUY:
            holdings[tx.symbol]["quantity"] += tx.quantity
            holdings[tx.symbol]["invested"] += (
                tx.quantity * tx.price + tx.fees
            )

        elif tx.transaction_type == TransactionType.SELL:
            holdings[tx.symbol]["quantity"] -= tx.quantity

    for symbol, data in holdings.items():
        current_price = get_current_price(symbol)

        if current_price is None:
            data["current_price"] = None
            data["current_value"] = None
            data["profit"] = None
            data["profit_percent"] = None
            continue

        data["current_price"] = round(current_price, 2)
        data["current_value"] = round(
            data["quantity"] * current_price, 2
        )

        data["profit"] = round(
            data["current_value"] - data["invested"], 2
        )

        if data["invested"] > 0:
            data["profit_percent"] = round(
                (data["profit"] / data["invested"]) * 100,
                2,
            )
        else:
            data["profit_percent"] = 0

    return holdings