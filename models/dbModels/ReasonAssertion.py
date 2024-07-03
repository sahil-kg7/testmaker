from sqlmodel import Field, SQLModel


class ReasonAssertion(SQLModel, table=True):
    __tablename__ = "reason_assertion"

    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    reason: str
    assertion: str
