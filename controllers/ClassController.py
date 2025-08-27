from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session
from db_config import get_db
from services.ClassService import ClassService
from models.dbModels import Class as dbClass
from utils import LogUtil
from exceptions import AppException, DatabaseException

router = APIRouter(
    prefix="/class",
    tags=["class"],
    responses={404: {"description": "Not found"}},
)

logger = LogUtil(__name__)


@router.get("/")
async def getClass(db: Session = Depends(get_db)):
    try:
        classService: ClassService = ClassService(db)
        return await classService.getClassList()
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to get class list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve class list",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while getting class list: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createClass(class_: dbClass, db: Session = Depends(get_db)) -> dbClass | None:
    try:
        classService: ClassService = ClassService(db)
        return await classService.createClass(class_)
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to create class: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create class",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while creating class: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e
