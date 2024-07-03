import uuid
from sqlmodel import Field, SQLModel


class QuestionImages(SQLModel, table=True):
    __tablename__ = "question_images"

    id: uuid.UUID = Field(primary_key=True)
    question_id: uuid.UUID = Field(foreign_key="question_details.id")
    position: int
    name: str | None = None
