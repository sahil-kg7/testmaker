from pydantic import BaseModel

from models import Question
from models.dbModels import (
    QuestionImages as dbQuestionImage,
    QuestionSubquestionMap as dbQuesSubquesMap,
    Test as dbTest,
    TestQuestionMap as dbTestQuesMap,
    TestSectionMap as dbTestSectionMap,
)


class TestModel(BaseModel):
    id: str | None = None  # uuid
    file_name: str
    school_id: str | None = None  # uuid
    class_number: int | None = None
    subject_id: str | None = None  # uuid
    test_type_id: str | None = None  # uuid
    section_count: int | None = None
    time_duration: int
    maximum_marks: int
    questions: list[Question] | None = None
    question_map: list[dbTestQuesMap] | None = None
    subquestion_map: list[dbQuesSubquesMap] | None = None
    section_map: list[dbTestSectionMap] | None = None
    question_images: list[dbQuestionImage] | None = None


def toTestModel(res) -> TestModel:
    return TestModel(
        id=res.id if "id" in res._fields else None,
        file_name=res.file_name if "file_name" in res._fields else None,
        school_id=res.school_id if "school_id" in res._fields else None,
        class_number=res.class_number if "class_number" in res._fields else None,
        subject_id=res.subject_id if "subject_id" in res._fields else None,
        test_type_id=res.test_type_id if "test_type_id" in res._fields else None,
        section_count=res.section_count if "section_count" in res._fields else None,
        time_duration=res.time_duration if "time_duration" in res._fields else None,
        maximum_marks=res.maximum_marks if "maximum_marks" in res._fields else None,
        questions=res.questions if "questions" in res._fields else None,
        question_map=res.question_map if "question_map" in res._fields else None,
        subquestion_map=(
            res.subquestion_map if "subquestion_map" in res._fields else None
        ),
        section_map=res.section_map if "section_map" in res._fields else None,
        question_images=(
            res.question_images if "question_images" in res._fields else None
        ),
    )


def toTestModelFromDbTest(res: dbTest) -> TestModel:
    return TestModel(
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
