# from fastapi import APIRouter, status
# from services import ClassService
# from models.dbModels import Class as dbClass

# router = APIRouter(
#     prefix="/class",
#     tags=["class"],
#     responses={404: {"description": "Not found"}},
# )


# @router.get("/")
# async def getClass():
#     return await ClassService.getClassList()


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def createClass(class_: dbClass) -> dbClass | None:
#     return await ClassService.createClass(class_)
