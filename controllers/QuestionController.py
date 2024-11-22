from fastapi import APIRouter, status
from sqlmodel import Session
from db_config import get_db
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


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def createQuestion(question: Question, db: Session = get_db) -> Question | None:
#     return await QuestionService.createQuestion(question, db)
