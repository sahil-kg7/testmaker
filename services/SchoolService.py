from sqlmodel import Session
from models.dbModels import School as dbSchool
from db.SchoolRepo import SchoolRepo


class SchoolService:
    def __init__(self, db: Session):
        self.db = db
        self.schoolRepo = SchoolRepo(db)

    async def getSchoolList(self):
        return await self.schoolRepo.getSchoolList()

    async def createSchool(self, school: dbSchool):
        return await self.schoolRepo.createSchool(school)
