from sqlmodel import Field, SQLModel


class Test(SQLModel, table=True):
    id: str = Field(primary_key=True)  # uuid
    file_name: str
    school_id: str = Field(foreign_key="school.id")  # uuid
    class_number: int = Field(foreign_key="class.class_number")
    subject_id: str = Field(foreign_key="subject.id")  # uuid
    test_type_id: str = Field(foreign_key="test_type.id")  # uuid
    section_count: int | None = None
    time_duration: int
    maximum_marks: int
