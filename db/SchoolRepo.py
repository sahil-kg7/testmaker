from sqlmodel import Session, select
from models.dbModels import School as dbSchool
from utils import LogUtil
from exceptions import DatabaseException


class SchoolRepo:
    def __init__(self, db: Session):
        self.db = db
        self.logger = LogUtil(__name__)

    async def getSchoolList(self):
        try:
            statement = select(dbSchool)
            result = self.db.exec(statement)
            schools = result.all()
            return schools
        except Exception as e:
            self.logger.error(
                f"Failed to fetch school list: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to fetch school list", original_exception=e
            ) from e

    async def createSchool(self, school: dbSchool) -> dbSchool:
        try:
            school_obj = dbSchool()
            self.db.add(school)
            self.db.expire_all()
            school_obj = self.db.exec(
                select(dbSchool).where(dbSchool.id == school.id)
            ).first()
            return school_obj
        except Exception as e:
            self.logger.error(
                f"Failed to create school: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create school", original_exception=e
            ) from e
