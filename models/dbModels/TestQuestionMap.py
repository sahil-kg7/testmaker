import uuid
from sqlmodel import Field, SQLModel


class TestQuestionMap(SQLModel, table=True):
    __tablename__ = "test_question_map"

    id: uuid.UUID = Field(primary_key=True)
    test_id: uuid.UUID = Field(foreign_key="test.id")
    question_id: uuid.UUID = Field(foreign_key="question_details.id")
    position: int
