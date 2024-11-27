import datetime
from sqlmodel import Field, SQLModel


class Fib(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    missing_word: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toFib(res) -> Fib:
    return Fib(
        id=res.id,
        question_id=res.question_id,
        missing_word=res.missing_word,
    )
