import uuid
from sqlmodel import Field, SQLModel


class QuestionSubquestionMap(SQLModel, table=True):
    __tablename__ = "question_subquestion_map"

    id: uuid.UUID = Field(primary_key=True)
    test_id: uuid.UUID = Field(foreign_key="test.id")
    question_id: uuid.UUID = Field(foreign_key="question_details.id")
    subquestion_id: uuid.UUID = Field(foreign_key="question_details.id")
    subquestion_number: int
