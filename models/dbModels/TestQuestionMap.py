from sqlmodel import Field, SQLModel


class TestQuestionMap(SQLModel, table=True):
    __tablename__ = "test_question_map"

    id: str = Field(primary_key=True)  # uuid
    test_id: str = Field(foreign_key="test.id")  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    position: int
