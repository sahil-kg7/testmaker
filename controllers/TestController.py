from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from db_config import get_db
from models import TestModel
from services.TestService import TestService

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getTest(page: int, db: Session = Depends(get_db)):
    try:
        testService: TestService = TestService(db)
        return await testService.getTestList(page)
    except Exception as e:
        print("Error occurred in controller while getting test list.", e.__str__())


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createTest(
    test: TestModel, db: Session = Depends(get_db)
) -> TestModel | None:
    try:
        testService: TestService = TestService(db)
        return await testService.createTest(test)
    except Exception as e:
        print("Error occurred in controller while creating test.", e.__str__())


@router.get("/types")
async def getTestTypes(db: Session = Depends(get_db)):
    try:
        testService: TestService = TestService(db)
        return await testService.getTestTypes()
    except Exception as e:
        print("Error occurred in controller while getting test types.", e.__str__())
