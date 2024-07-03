from sqlmodel import Field, SQLModel


class QuestionType(SQLModel, table=True):
    __tablename__ = "question_type"

    id: int = Field(primary_key=True)
    name: str
