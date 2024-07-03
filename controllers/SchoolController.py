from fastapi import APIRouter, status
from services import SchoolService
from models.dbModels import School as dbSchool

router = APIRouter(
    prefix="/school",
    tags=["school"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_school():
    return await SchoolService.get_school_list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_school(school: dbSchool) -> dbSchool | None:
    return await SchoolService.create_school(school)
