from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from db_config import get_db
from models import Question
from services.QuestionService import QuestionService

router = APIRouter(
    prefix="/question",
    tags=["question"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK)
async def getQuestionList(db: Session = Depends(get_db)):
    questionService: QuestionService = QuestionService(db)
    return await questionService.getQuestionList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createQuestion(
    question: Question, db: Session = Depends(get_db)
) -> Question | None:
    questionService: QuestionService = QuestionService(db)
    return await questionService.createQuestion(question)
