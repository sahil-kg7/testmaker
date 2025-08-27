from sqlmodel import Session
from models.dbModels import School as dbSchool
from db.SchoolRepo import SchoolRepo
from utils import LogUtil
from exceptions import AppException


class SchoolService:
    def __init__(self, db: Session):
        self.db = db
        self.schoolRepo = SchoolRepo(db)
        self.logger = LogUtil(__name__)

    async def getSchoolList(self):
        try:
            return await self.schoolRepo.getSchoolList()
        except Exception as e:
            self.logger.error(
                f"Failed to get school list: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to get school list",
                original_exception=e,
            ) from e

    async def createSchool(self, school: dbSchool):
        try:
            return await self.schoolRepo.createSchool(school)
        except Exception as e:
            self.logger.error(
                f"Failed to create school: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create school",
                original_exception=e,
            ) from e
