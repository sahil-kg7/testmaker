import uuid
from sqlmodel import Field, SQLModel


class TestType(SQLModel, table=True):
    __tablename__ = "test_type"

    id: uuid.UUID = Field(primary_key=True)
    type: str
