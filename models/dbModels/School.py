import uuid
from sqlmodel import Field, SQLModel


class School(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    name: str
    logo_filename: str | None = None
