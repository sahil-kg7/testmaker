import datetime
from sqlmodel import Field, SQLModel


class Class(SQLModel, table=True):
    class_number: int = Field(primary_key=True)
    class_roman: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)
