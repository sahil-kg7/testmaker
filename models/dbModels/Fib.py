from sqlmodel import Field, SQLModel


class Fib(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    question_id: str = Field(foreign_key="question_details.id")  # uuid
    missing_word: str
