from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_invested: float
    current_value: float
    profit_loss: float
    profit_percent: float
    total_assets: int