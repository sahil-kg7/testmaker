from sqlmodel import Field, SQLModel


class MatchA(SQLModel, table=True):
    __tablename__ = "match_a"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    option: str
