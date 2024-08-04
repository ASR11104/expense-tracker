from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, message_id: int):
    return db.query(models.ExpenseMessage).filter(models.ExpenseMessage.id == message_id).first()

def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ExpenseMessage).offset(skip).limit(limit).all()

def create_message(db: Session, expense_message: schemas.MessageCreate):
    db_message = models.ExpenseMessage(message=expense_message.message)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(amount=expense.amount)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense