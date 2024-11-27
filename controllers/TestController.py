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
    testService: TestService = TestService(db)
    return await testService.getTestList(page)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createTest(
    test: TestModel, db: Session = Depends(get_db)
) -> TestModel | None:
    testService: TestService = TestService(db)
    return await testService.createTest(test)


@router.get("/types")
async def getTestTypes(db: Session = Depends(get_db)):
    testService: TestService = TestService(db)
    return await testService.getTestTypes()
