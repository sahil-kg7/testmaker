from datetime import datetime
from sqlmodel import Field, SQLModel


class QuestionDetails(SQLModel, table=True):
    __tablename__ = "question_details"

    id: str = Field(primary_key=True)  # uuid
    question_type_id: int = Field(foreign_key="question_type.id")
    subject_id: str = Field(foreign_key="subject.id")  # uuid
    difficulty: str = Field(foreign_key="question_difficulty.id")  # uuid
    marks: int
    content: str | None = None
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toQuestionDetails(res) -> QuestionDetails:
    return QuestionDetails(
        id=res.id,
        question_type_id=res.question_type_id,
        subject_id=res.subject_id,
        difficulty=res.difficulty,
        marks=res.marks,
        content=res.content,
        created_on=res.created_on,
        updated_on=res.updated_on,
    )
