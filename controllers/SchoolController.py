from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db_config import get_db
from services.SchoolService import SchoolService
from models.dbModels import School as dbSchool
from utils import LogUtil
from exceptions import AppException, DatabaseException

router = APIRouter(
    prefix="/school",
    tags=["school"],
    responses={404: {"description": "Not found"}},
)

logger = LogUtil(__name__)


@router.get("/")
async def getSchool(db: Session = Depends(get_db)):
    try:
        schoolService: SchoolService = SchoolService(db)
        return await schoolService.getSchoolList()
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to get school list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve school list",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while getting school list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createSchool(
    school: dbSchool, db: Session = Depends(get_db)
) -> dbSchool | None:
    try:
        schoolService: SchoolService = SchoolService(db)
        return await schoolService.createSchool(school)
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to create school: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create school",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while creating school: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e
