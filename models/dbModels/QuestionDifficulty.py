import uuid
from sqlmodel import Field, SQLModel


class QuestionDifficulty(SQLModel, table=True):
    __tablename__ = "question_difficulty"

    id: uuid.UUID = Field(primary_key=True)
    level: str
