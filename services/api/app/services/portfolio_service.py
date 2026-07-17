from sqlalchemy.orm import Session
from app.models.portfolio import Portfolio

#  1. FIXED IMPORT PATH
from app.repositories.portfolio_repository import PortfolioRepository


def create_portfolio(
    db: Session,
    name: str,
    user_id: int,
):
    portfolio = Portfolio(name=name, user_id=user_id)
    
    #  Using repository pattern for creation
    repo = PortfolioRepository(db)
    repo.create(portfolio)
    return portfolio


def get_portfolios(
    db: Session,
    user_id: int,
):
    repo = PortfolioRepository(db)
    return repo.get_by_user(user_id)


def get_portfolio(
    db: Session,
    portfolio_id: int,
    user_id: int,
):
    #  2. FIXED SYNTAX ERROR: Split assignment and return logic cleanly
    repo = PortfolioRepository(db)
    
    # Note: Assuming your repository method internally handles filtering by user/id.
    # If get_by_id doesn't handle user filtering, use your repository query instance.
    return repo.get_by_id_and_user(portfolio_id, user_id)


def update_portfolio(
    db: Session,
    portfolio: Portfolio,
    name: str,
):
    portfolio.name = name
    
    #  Using repository pattern for updates
    repo = PortfolioRepository(db)
    repo.update(portfolio)
    return portfolio


def delete_portfolio(
    db: Session,
    portfolio: Portfolio,
):
    #  Using repository pattern for deletion
    repo = PortfolioRepository(db)
    repo.delete(portfolio)


def get_portfolio_by_id(
    db: Session,
    portfolio_id: int,
):
    #  Using repository pattern for lookups
    repo = PortfolioRepository(db)
    return repo.get_by_id(portfolio_id)
