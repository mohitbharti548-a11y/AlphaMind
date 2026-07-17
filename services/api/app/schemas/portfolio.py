from pydantic import BaseModel
from pydantic import ConfigDict

class PortfolioCreate(BaseModel):
    name: str

    model_config = ConfigDict(
        populate_by_name = True
    )

class PortfolioResponse(BaseModel):
    id: int
    name: str
    user_id: int

    model_config = ConfigDict(
        from_attributes = True
    )

class PortfolioUpdate(BaseModel):
    name: str        