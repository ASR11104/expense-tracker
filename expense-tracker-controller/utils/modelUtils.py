

from model.model import NLPModel
from database import crud, models, schemas


def process_message(db, message):
    model = NLPModel()
    ents = model.get_attributes(message)

    for ent in ents:
        print(ent.label_, ent.text)
        amount = int(ent.text)
        expense = schemas.ExpenseCreate(amount=amount)
        create_expense_db_entry(db, expense)

def create_expense_db_entry(db, expense: schemas.ExpenseCreate):
    crud.create_expense(db=db, expense=expense)

