from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session

from db_config import get_db
from models import TestModel
from services.TestService import TestService
from utils import LogUtil
from exceptions import AppException, DatabaseException

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

logger = LogUtil(__name__)


@router.get("/")
async def getTest(page: int, db: Session = Depends(get_db)):
    try:
        testService: TestService = TestService(db)
        return await testService.getTestList(page)
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to get test list for page {page}: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve test list",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while getting test list for page {page}: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createTest(
    test: TestModel, db: Session = Depends(get_db)
) -> TestModel | None:
    try:
        testService: TestService = TestService(db)
        return await testService.createTest(test)
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to create test: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create test",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while creating test: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e


@router.get("/types")
async def getTestTypes(db: Session = Depends(get_db)):
    try:
        testService: TestService = TestService(db)
        return await testService.getTestTypes()
    except (AppException, DatabaseException) as e:
        logger.error(
            f"Failed to get test types: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve test types",
        ) from e
    except Exception as e:
        logger.error(
            f"Unexpected error while getting test types: {e.__str__()}",
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        ) from e
