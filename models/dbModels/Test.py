import uuid
from sqlmodel import Field, SQLModel


class Test(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True)
    file_name: str
    school_id: uuid.UUID = Field(foreign_key="school.id")
    class_number: int = Field(foreign_key="class.class_number")
    subject_id: uuid.UUID = Field(foreign_key="subject.id")
    test_type_id: uuid.UUID = Field(foreign_key="test_type.id")
    section_count: int | None = None
    time_duration: int
    maximum_marks: int
