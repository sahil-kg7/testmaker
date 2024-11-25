from sqlmodel import Field, SQLModel


class TestSectionMap(SQLModel, table=True):
    __tablename__ = "test_section_map"

    id: str = Field(primary_key=True)  # uuid
    test_id: str = Field(foreign_key="test.id")  # uuid
    section_number: int = Field(default=0)
    initial_ques_number: int = Field(default=0)


def toTestSectionMap(res) -> TestSectionMap:
    return TestSectionMap(
        test_id=res.test_id,
        section_number=res.section,
        initial_ques_number=res.initial_ques_number,
    )
