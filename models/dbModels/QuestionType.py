import datetime
from sqlmodel import Field, SQLModel


class QuestionType(SQLModel, table=True):
    __tablename__ = "question_type"

    id: int = Field(primary_key=True)
    name: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)
