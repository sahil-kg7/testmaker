from sqlmodel import Session, select
from models.dbModels import Subject as dbSubject


class SubjectRepo:
    def __init__(self, db: Session):
        self.db = db

    async def getSubjectList(self):
        return self.db.exec(select(dbSubject)).all()

    async def createSubject(self, subject: dbSubject) -> dbSubject:
        subject_obj = dbSubject()
        self.db.add(subject)
        self.db.expire_all()
        subject_obj = self.db.exec(
            select(dbSubject).where(dbSubject.id == subject.id)
        ).first()
        return subject_obj
