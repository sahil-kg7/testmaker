from sqlmodel import Session, select
from models.dbModels import School as dbSchool


class SchoolRepo:
    def __init__(self, db: Session):
        self.db = db

    async def getSchoolList(self):
        return self.db.exec(select(dbSchool)).all()

    async def createSchool(self, school: dbSchool) -> dbSchool:
        school_obj = dbSchool()
        self.db.add(school)
        self.db.expire_all()
        school_obj = self.db.exec(
            select(dbSchool).where(dbSchool.id == school.id)
        ).first()
        return school_obj
