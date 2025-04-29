from sqlmodel import Session, select
from models.dbModels import Class as dbClass


class ClassRepo:
    def __init__(self, db: Session):
        self.db = db

    async def getClassList(self):
        return self.db.exec(select(dbClass)).all()

    async def createClass(self, class_: dbClass) -> dbClass | None:
        self.db.add(class_)
        self.db.expire_all()
        class_obj = self.db.exec(
            select(dbClass).where(dbClass.class_number == class_.class_number)
        ).first()
        return class_obj
