from sqlmodel import Session, select
from models.dbModels import Class as dbClass
from utils import LogUtil
from exceptions import DatabaseException


class ClassRepo:
    def __init__(self, db: Session):
        self.db = db
        self.logger = LogUtil(__name__)

    async def getClassList(self):
        try:
            statement = select(dbClass)
            result = self.db.exec(statement)
            classes = result.all()
            return classes
        except Exception as e:
            self.logger.error(
                f"Failed to fetch class list: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to fetch class list", original_exception=e
            ) from e

    async def createClass(self, class_: dbClass) -> dbClass | None:
        try:
            self.db.add(class_)
            self.db.expire_all()
            class_obj = self.db.exec(
                select(dbClass).where(dbClass.class_number == class_.class_number)
            ).first()
            return class_obj
        except Exception as e:
            self.logger.error(
                f"Failed to create class: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create class", original_exception=e
            ) from e
