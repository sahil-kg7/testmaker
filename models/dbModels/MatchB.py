from datetime import datetime
from sqlmodel import Field, SQLModel


class MatchB(SQLModel, table=True):
    __tablename__ = "match_b"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    match_option: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toMatchB(res) -> MatchB:
    return MatchB(
        id=res.id,
        question_id=res.question_id,
        match_option=res.match_option,
    )
