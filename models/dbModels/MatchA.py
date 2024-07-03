import uuid
from sqlmodel import Field, SQLModel


class MatchA(SQLModel, table=True):
    __tablename__ = "match_a"

    id: uuid.UUID = Field(primary_key=True)
    question_id: uuid.UUID = Field(foreign_key="question_details.id")
    option: str
