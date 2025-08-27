from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db_config import get_db
from models import Question
from services.QuestionService import QuestionService
from utils import LogUtil
from exceptions import AppException, DatabaseException

router = APIRouter(
    prefix="/question",
    tags=["question"],
    responses={404: {"description": "Not found"}},
)

logger = LogUtil(__name__)


@router.get("/", status_code=status.HTTP_200_OK)
async def getQuestionList(db: Session = Depends(get_db)):
    try:
        questionService: QuestionService = QuestionService(db)
        return await questionService.getQuestionList()
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to get question list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve question list",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while getting question list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createQuestion(
    question: Question, db: Session = Depends(get_db)
) -> Question | None:
    try:
        questionService: QuestionService = QuestionService(db)
        return await questionService.createQuestion(question)
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to create question: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create question",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while creating question: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e
