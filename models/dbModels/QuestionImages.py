from sqlmodel import Field, SQLModel


class QuestionImages(SQLModel, table=True):
    __tablename__ = "question_images"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    position: int
    name: str | None = None
