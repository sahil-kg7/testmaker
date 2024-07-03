import uuid
from sqlmodel import Field, SQLModel


class QuestionDetails(SQLModel, table=True):
    __tablename__ = "question_details"

    id: uuid.UUID = Field(primary_key=True)
    question_type_id: int = Field(foreign_key="question_type.id")
    subject_id: uuid.UUID = Field(foreign_key="subject.id")
    difficulty: uuid.UUID = Field(foreign_key="question_difficulty.id")
    marks: int
    content: str | None = None
