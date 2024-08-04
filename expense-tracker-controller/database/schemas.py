from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True

class ExpenseBase(BaseModel):
    amount: int


class ExpenseCreate(ExpenseBase):
    pass
    

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True