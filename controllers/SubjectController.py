from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db_config import get_db
from services.SubjectService import SubjectService
from models.dbModels import Subject as dbSubject
from utils import LogUtil
from exceptions import AppException, DatabaseException

router = APIRouter(
    prefix="/subject",
    tags=["subject"],
    responses={404: {"description": "Not found"}},
)

logger = LogUtil(__name__)


@router.get("/")
async def getSubject(db: Session = Depends(get_db)):
    try:
        subjectService: SubjectService = SubjectService(db)
        return await subjectService.getSubjectList()
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to get subject list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve subject list",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while getting subject list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createSubject(
    subject: dbSubject, db: Session = Depends(get_db)
) -> dbSubject | None:
    try:
        subjectService: SubjectService = SubjectService(db)
        return await subjectService.createSubject(subject)
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to create subject: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create subject",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while creating subject: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e
