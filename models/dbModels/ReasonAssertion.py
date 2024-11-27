import datetime
from sqlmodel import Field, SQLModel


class ReasonAssertion(SQLModel, table=True):
    __tablename__ = "reason_assertion"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    reason_statement: str
    assertion_statement: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toReasonAssertion(res) -> ReasonAssertion:
    return ReasonAssertion(
        id=res.id,
        question_id=res.question_id,
        reason_statement=res.reason_statement,
        assertion_statement=res.assertion_statement,
    )
