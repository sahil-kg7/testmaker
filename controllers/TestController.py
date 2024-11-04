from fastapi import APIRouter, status

from models import TestModel
from services import TestService

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getTest():
    return await TestService.getTestList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createTest(test: TestModel) -> TestModel | None:
    return await TestService.createTest(test)


@router.get("/types")
async def getTestTypes():
    return await TestService.getTestTypes()
