import datetime
from sqlmodel import Field, SQLModel


class Mcq(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    option_text: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toMcq(res) -> Mcq:
    return Mcq(
        id=res.id,
        question_id=res.question_id,
        option_text=res.option_text,
    )
