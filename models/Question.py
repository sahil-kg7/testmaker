from pydantic import BaseModel

from models.dbModels import Fib, MatchA, MatchB, Mcq, ReasonAssertion


class Question(BaseModel):
    id: str | None = None  # uuid
    question_type_id: int
    subject_id: str | None = None  # uuid
    difficulty: str | None = None  # uuid
    marks: int
    content: str | None = None
    fib_missing_word: list[Fib] | None = None
    match_a_option: list[MatchA] | None = None
    match_b_option: list[MatchB] | None = None
    mcq_option: list[Mcq] | None = None
    reason_assertion: ReasonAssertion | None = None


def toQuestion(res) -> Question:
    return Question(
        id=res.id if "id" in res._fields else None,
        question_type_id=(
            res.question_type_id if "question_type_id" in res._fields else None
        ),
        subject_id=res.subject_id if "subject_id" in res._fields else None,
        difficulty=res.difficulty if "difficulty" in res._fields else None,
        marks=res.marks if "marks" in res._fields else None,
        content=res.content if "content" in res._fields else None,
        fib_missing_word=(
            res.fib_missing_word if "fib_missing_word" in res._fields else None
        ),
        match_a_option=res.match_a_option if "match_a_option" in res._fields else None,
        match_b_option=res.match_b_option if "match_b_option" in res._fields else None,
        mcq_option=res.mcq_option if "mcq_option" in res._fields else None,
        reason_assertion=(
            res.reason_assertion if "reason_assertion" in res._fields else None
        ),
    )
