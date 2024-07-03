import uuid
from models.dbModels import Subject as dbSubject
from db import SubjectRepo


async def get_subject_list():
    return await SubjectRepo.get_subject_list()


async def create_subject(subject: dbSubject):
    subject.id = uuid.uuid4()
    return await SubjectRepo.create_subject(subject)
