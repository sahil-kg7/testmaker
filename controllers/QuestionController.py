from fastapi import APIRouter, status
from models import Question
from services import QuestionService

router = APIRouter(
    prefix="/question",
    tags=["question"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_question_list():
    return await QuestionService.get_question_list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_question(question: Question) -> Question | None:
    return await QuestionService.create_question(question)
