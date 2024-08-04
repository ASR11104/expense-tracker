from fastapi import Depends, FastAPI, BackgroundTasks
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine
from utils.modelUtils import process_message

models.Base.metadata.create_all(bind=engine)

from model.model import NLPModel

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/message/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db),):
    background_tasks.add_task(process_message, db, message.message)
    return crud.create_message(db=db, expense_message=message)
