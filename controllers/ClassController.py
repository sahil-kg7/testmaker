from fastapi import APIRouter, status
from services import ClassService
from models.dbModels import Class as dbClass

router = APIRouter(
    prefix="/class",
    tags=["class"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_class():
    return await ClassService.get_class_list()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_class(class_: dbClass) -> dbClass | None:
    return await ClassService.create_class(class_)
