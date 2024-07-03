from sqlmodel import Field, SQLModel


class Class(SQLModel, table=True):
    class_number: int = Field(primary_key=True)
    class_roman: str
