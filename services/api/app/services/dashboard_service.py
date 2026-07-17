from app.services.analytics_service import calculate_holdings


def get_dashboard(db, portfolio_id):

    holdings = calculate_holdings(
        db,
        portfolio_id,
    )

    invested = 0
    current = 0

    for asset in holdings.values():

        invested += asset["invested"]
        current += asset.get(
            "current_value",
            0,
        )

    profit = current - invested

    percent = 0

    if invested > 0:
        percent = (
            profit / invested
        ) * 100

    return {
        "total_invested": round(invested, 2),
        "current_value": round(current, 2),
        "profit_loss": round(profit, 2),
        "profit_percent": round(percent, 2),
        "total_assets": len(holdings),
    }