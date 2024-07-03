import uuid
from sqlmodel import Field, SQLModel


class TestSectionMap(SQLModel, table=True):
    __tablename__ = "test_section_map"

    id: uuid.UUID = Field(primary_key=True)
    test_id: uuid.UUID = Field(foreign_key="test.id")
    section: int = Field(default=0)
    initial_ques_number: int = Field(default=0)
