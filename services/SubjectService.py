import uuid
from models.dbModels import Subject as dbSubject
from db import SubjectRepo


async def getSubjectList():
    return await SubjectRepo.getSubjectList()


async def createSubject(subject: dbSubject):
    subject.id = uuid.uuid4()
    return await SubjectRepo.createSubject(subject)
