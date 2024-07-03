from sqlmodel import Field, SQLModel


class TestSectionMap(SQLModel, table=True):
    __tablename__ = "test_section_map"

    id: str = Field(primary_key=True)  # uuid
    test_id: str = Field(foreign_key="test.id")  # uuid
    section: int = Field(default=0)
    initial_ques_number: int = Field(default=0)
