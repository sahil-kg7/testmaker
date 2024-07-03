from fastapi import APIRouter, status
from services import SubjectService
from models.dbModels import Subject as dbSubject

router = APIRouter(
    prefix="/subject",
    tags=["subject"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_subject():
    return await SubjectService.get_subject_list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_subject(subject: dbSubject) -> dbSubject | None:
    return await SubjectService.create_subject(subject)
