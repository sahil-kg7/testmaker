from typing import List
from pydantic import BaseModel

from models import Question
from models.dbModels import (
    QuestionImages,
    QuestionSubquestionMap,
    TestQuestionMap,
    TestSectionMap,
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
    questions: List[Question] | None = None
    question_map: List[TestQuestionMap] | None = None
    subquestion_map: List[QuestionSubquestionMap] | None = None
    section_map: List[TestSectionMap] | None = None
    question_images: List[QuestionImages] | None = None
