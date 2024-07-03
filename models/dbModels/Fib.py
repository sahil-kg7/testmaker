import uuid
from sqlmodel import Field, SQLModel


class Fib(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    question_id: uuid.UUID = Field(foreign_key="question_details.id")
    missing_word: str
