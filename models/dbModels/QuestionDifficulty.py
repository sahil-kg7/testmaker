from sqlmodel import Field, SQLModel


class QuestionDifficulty(SQLModel, table=True):
    __tablename__ = "question_difficulty"

    id: str = Field(primary_key=True)  # uuid
    level: str
