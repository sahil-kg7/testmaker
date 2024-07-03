from sqlmodel import Field, SQLModel


class School(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    name: str
    logo_filename: str | None = None
