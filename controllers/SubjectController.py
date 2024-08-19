from fastapi import APIRouter, status
from services import SubjectService
from models.dbModels import Subject as dbSubject

router = APIRouter(
    prefix="/subject",
    tags=["subject"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getSubject():
    return await SubjectService.getSubjectList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createSubject(subject: dbSubject) -> dbSubject | None:
    return await SubjectService.createSubject(subject)
