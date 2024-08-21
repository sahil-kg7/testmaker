from sqlmodel import Field, SQLModel


class MatchA(SQLModel, table=True):
    __tablename__ = "match_a"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    match_option: str


def toMatchA(res) -> MatchA:
    return MatchA(id=res.id, question_id=res.question_id, match_option=res.match_option)
