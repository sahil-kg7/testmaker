from sqlmodel import Field, SQLModel


class QuestionSubquestionMap(SQLModel, table=True):
    __tablename__ = "question_subquestion_map"

    id: str = Field(primary_key=True)  # uuid
    test_id: str = Field(foreign_key="test.id")  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    subquestion_id: str = Field(foreign_key="question_details.id")  # uuid
    subquestion_number: int


def toQuestionSubquestionMap(res) -> QuestionSubquestionMap:
    return QuestionSubquestionMap(
        test_id=res.test_id,
        question_id=res.question_id,
        subquestion_id=res.subquestion_id,
        subquestion_number=res.subquestion_number,
    )
