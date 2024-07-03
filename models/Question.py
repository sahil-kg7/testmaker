import uuid
from typing import List
from pydantic import BaseModel


class Question(BaseModel):
    id: uuid.UUID | None = None
    question_type_id: int
    subject_id: uuid.UUID | None = None  # remove none later
    difficulty: uuid.UUID | None = None  # remove none later
    marks: int
    content: str | None = None
    fib_missing_word: List[str] | None = None
    match_a_option: List[str] | None = None
    match_b_option: List[str] | None = None
    mcq_option: List[str] | None = None
    reason: str | None = None
    assertion: str | None = None
