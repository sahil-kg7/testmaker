from sqlmodel import Field, SQLModel


class QuestionDetails(SQLModel, table=True):
    __tablename__ = "question_details"

    id: str = Field(primary_key=True)  # uuid
    question_type_id: int = Field(foreign_key="question_type.id")
    subject_id: str = Field(foreign_key="subject.id")  # uuid
    difficulty: str = Field(foreign_key="question_difficulty.id")  # uuid
    marks: int
    content: str | None = None
