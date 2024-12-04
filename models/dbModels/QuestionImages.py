from datetime import datetime
from sqlmodel import Field, SQLModel


class QuestionImages(SQLModel, table=True):
    __tablename__ = "question_images"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    image_position: int
    image_name: str | None = None
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toQuestionImages(res) -> QuestionImages:
    return QuestionImages(
        question_id=res.question_id,
        image_position=res.position,
        image_name=res.image_name,
    )
