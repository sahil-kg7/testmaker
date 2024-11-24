from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from db_config import get_db
from services.SubjectService import SubjectService
from models.dbModels import Subject as dbSubject

router = APIRouter(
    prefix="/subject",
    tags=["subject"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getSubject(db: Session = Depends(get_db)):
    subjectService: SubjectService = SubjectService(db)
    return await subjectService.getSubjectList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createSubject(
    subject: dbSubject, db: Session = Depends(get_db)
) -> dbSubject | None:
    subjectService: SubjectService = SubjectService(db)
    return await subjectService.createSubject(subject)
