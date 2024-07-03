from sqlmodel import Field, SQLModel


class Subject(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    name: str
