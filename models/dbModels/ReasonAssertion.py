import uuid
from sqlmodel import Field, SQLModel


class ReasonAssertion(SQLModel, table=True):
    __tablename__ = "reason_assertion"

    id: uuid.UUID = Field(primary_key=True)
    question_id: uuid.UUID = Field(foreign_key="question_details.id")
    reason: str
    assertion: str
