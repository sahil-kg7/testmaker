from fastapi import APIRouter, status
from services import SchoolService
from models.dbModels import School as dbSchool

router = APIRouter(
    prefix="/school",
    tags=["school"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getSchool():
    return await SchoolService.getSchoolList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createSchool(school: dbSchool) -> dbSchool | None:
    return await SchoolService.createSchool(school)
