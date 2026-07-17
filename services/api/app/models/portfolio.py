from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="portfolios",
    )
    assets = relationship(
    "Asset",
    back_populates="portfolio",
    cascade="all, delete",
    )
    transactions = relationship(
    "Transaction",
    back_populates="portfolio",
    cascade="all, delete-orphan",
)