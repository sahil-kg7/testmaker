from sqlmodel import Session, select
from models.dbModels import Subject as dbSubject
from utils import LogUtil
from exceptions import DatabaseException


class SubjectRepo:
    def __init__(self, db: Session):
        self.db = db
        self.logger = LogUtil(__name__)

    async def getSubjectList(self):
        try:
            statement = select(dbSubject)
            result = self.db.exec(statement)
            subjects = result.all()
            return subjects
        except Exception as e:
            self.logger.error(
                f"Failed to fetch subject list: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to fetch subject list", original_exception=e
            ) from e

    async def createSubject(self, subject: dbSubject) -> dbSubject:
        try:
            subject_obj = dbSubject()
            self.db.add(subject)
            self.db.expire_all()
            subject_obj = self.db.exec(
                select(dbSubject).where(dbSubject.id == subject.id)
            ).first()
            return subject_obj
        except Exception as e:
            self.logger.error(
                f"Failed to create subject: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create subject", original_exception=e
            ) from e
