from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from db_config import get_db
from services.ClassService import ClassService
from models.dbModels import Class as dbClass

router = APIRouter(
    prefix="/class",
    tags=["class"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def getClass(db: Session = Depends(get_db)):
    classService: ClassService = ClassService(db)
    return await classService.getClassList()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def createClass(class_: dbClass, db: Session = Depends(get_db)) -> dbClass | None:
    classService: ClassService = ClassService(db)
    return await classService.createClass(class_)
