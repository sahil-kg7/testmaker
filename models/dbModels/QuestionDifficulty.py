import datetime
from sqlmodel import Field, SQLModel


class QuestionDifficulty(SQLModel, table=True):
    __tablename__ = "question_difficulty"

    id: str = Field(primary_key=True)  # uuid
    level: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)
