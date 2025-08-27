from sqlmodel import Session
from models.dbModels import Class as dbClass
from db.ClassRepo import ClassRepo
from utils import LogUtil
from exceptions import AppException


class ClassService:
    def __init__(self, db: Session):
        self.db = db
        self.classRepo = ClassRepo(db)
        self.logger = LogUtil(__name__)

    async def getClassList(self):
        try:
            return await self.classRepo.getClassList()
        except Exception as e:
            self.logger.error(
                f"Failed to get class list: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to get class list",
                original_exception=e,
            ) from e

    async def createClass(self, class_: dbClass) -> dbClass | None:
        try:
            return await self.classRepo.createClass(class_)
        except Exception as e:
            self.logger.error(
                f"Failed to create class: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create class",
                original_exception=e,
            ) from e
