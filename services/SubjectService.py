import uuid
from models.dbModels import Subject as dbSubject
from db.SubjectRepo import SubjectRepo


class SubjectService:
    def __init__(self, db):
        self.db = db
        self.subjectRepo = SubjectRepo(db)

    async def getSubjectList(self):
        return await self.subjectRepo.getSubjectList()

    async def createSubject(self, subject: dbSubject):
        subject.id = uuid.uuid4().__str__()
        return await self.subjectRepo.createSubject(subject)
