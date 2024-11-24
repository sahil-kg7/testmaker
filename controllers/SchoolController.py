from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from db_config import get_db
from services.SchoolService import SchoolService
from models.dbModels import School as dbSchool

router = APIRouter(
    prefix="/school",
    tags=["school"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getSchool(db: Session = Depends(get_db)):
    schoolService: SchoolService = SchoolService(db)
    return await schoolService.getSchoolList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createSchool(
    school: dbSchool, db: Session = Depends(get_db)
) -> dbSchool | None:
    schoolService: SchoolService = SchoolService(db)
    return await schoolService.createSchool(school)
