import uuid
from sqlmodel import Field, SQLModel


class Subject(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    name: str
