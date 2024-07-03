from sqlmodel import Field, SQLModel


class TestType(SQLModel, table=True):
    __tablename__ = "test_type"

    id: str = Field(primary_key=True)  # uuid
    type: str
