from datetime import datetime, UTC

from sqlalchemy import DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import AssetType, TransactionType
from app.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    symbol: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    asset_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    asset_type: Mapped[AssetType] = mapped_column(
        Enum(AssetType),
        nullable=False,
    )

    transaction_type: Mapped[TransactionType] = mapped_column(
        Enum(TransactionType),
        nullable=False,
    )

    quantity: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    fees: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    transaction_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    portfolio_id: Mapped[int] = mapped_column(
        ForeignKey("portfolios.id"),
        nullable=False,
    )

    portfolio = relationship(
        "Portfolio",
        back_populates="transactions",
    )