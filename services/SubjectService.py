import uuid
from sqlmodel import Session
from models.dbModels import Subject as dbSubject
from db.SubjectRepo import SubjectRepo
from utils import LogUtil
from exceptions import AppException


class SubjectService:
    def __init__(self, db: Session):
        self.db = db
        self.subjectRepo = SubjectRepo(db)
        self.logger = LogUtil(__name__)

    async def getSubjectList(self):
        try:
            return await self.subjectRepo.getSubjectList()
        except Exception as e:
            self.logger.error(
                f"Failed to get subject list: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to get subject list",
                original_exception=e,
            ) from e

    async def createSubject(self, subject: dbSubject):
        try:
            subject.id = uuid.uuid4().__str__()
            return await self.subjectRepo.createSubject(subject)
        except Exception as e:
            self.logger.error(
                f"Failed to create subject: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create subject",
                original_exception=e,
            ) from e
