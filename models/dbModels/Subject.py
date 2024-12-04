from datetime import datetime
from sqlmodel import Field, SQLModel


class Subject(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    name: str
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)
