from sqlalchemy import Column, Integer, String
from database import Base


class SpimexTradingResults(Base):
    __tablename__ = "spimex_trading_results"