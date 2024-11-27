import datetime
from sqlmodel import Field, SQLModel


class TestType(SQLModel, table=True):
    __tablename__ = "test_type"

    id: str = Field(primary_key=True)  # uuid
    type: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)
