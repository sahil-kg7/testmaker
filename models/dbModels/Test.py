import datetime
from sqlmodel import Field, SQLModel


class Test(SQLModel, table=True):
    __tablename__ = "test"

    id: str = Field(primary_key=True)  # uuid
    file_name: str
    school_id: str = Field(foreign_key="school.id")  # uuid
    class_number: int = Field(foreign_key="class.class_number")
    subject_id: str = Field(foreign_key="subject.id")  # uuid
    test_type_id: str = Field(foreign_key="test_type.id")  # uuid
    section_count: int | None = None
    time_duration: int
    maximum_marks: int
    created_on: datetime = Field(default_factory=datetime.now)
    updated_on: datetime = Field(default_factory=datetime.now)


def toTest(res) -> Test:
    return Test(
        id=res.id,
        file_name=res.file_name,
        school_id=res.school_id,
        class_number=res.class_number,
        subject_id=res.subject_id,
        test_type_id=res.test_type_id,
        section_count=res.section_count,
        time_duration=res.time_duration,
        maximum_marks=res.maximum_marks,
    )
