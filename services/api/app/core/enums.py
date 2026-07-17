from enum import Enum


class AssetType(str, Enum):
    STOCK = "STOCK"
    ETF = "ETF"
    CRYPTO = "CRYPTO"
    GOLD = "GOLD"
    MUTUAL_FUND = "MUTUAL_FUND"


class TransactionType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"