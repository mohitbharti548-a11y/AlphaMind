from app.services.market_service import get_current_price

price = get_current_price("AAPL")

print(price)