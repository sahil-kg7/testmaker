from sqlmodel import Field, SQLModel


class TestQuestionMap(SQLModel, table=True):
    __tablename__ = "test_question_map"

    id: str = Field(primary_key=True)  # uuid
    test_id: str = Field(foreign_key="test.id")  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    question_position: int


def toTestQuestionMap(res) -> TestQuestionMap:
    return TestQuestionMap(
        test_id=res.test_id,
        question_id=res.question_id,
        question_position=res.position,
    )
