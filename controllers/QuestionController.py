from fastapi import APIRouter, status
from models import Question
from services import QuestionService

router = APIRouter(
    prefix="/question",
    tags=["question"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK)
async def getQuestionList():
    return await QuestionService.getQuestionList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createQuestion(question: Question) -> Question | None:
    return await QuestionService.createQuestion(question)
