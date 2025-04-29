from sqlmodel import Session
from models.dbModels import Class as dbClass
from db.ClassRepo import ClassRepo


class ClassService:
    def __init__(self, db: Session):
        self.db = db
        self.classRepo = ClassRepo(db)

    async def getClassList(self):
        return await self.classRepo.getClassList()

    async def createClass(self, class_: dbClass) -> dbClass | None:
        return await self.classRepo.createClass(class_)
