from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from .database import Base


class ExpenseMessage(Base):
    __tablename__ = "expense_messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    