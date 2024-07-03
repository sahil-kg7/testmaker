from typing import List
from db_config import sql_engine
from sqlmodel import Session, select
from models.dbModels import Subject as dbSubject

engine = sql_engine()


async def get_subject_list():
    subjectList: List[dbSubject] = []
    with Session(engine) as session:
        subjectList = session.exec(select(dbSubject)).all()
        session.close()
    return subjectList


async def create_subject(subject: dbSubject) -> dbSubject:
    subject_obj = dbSubject()
    with Session(engine) as session:
        session.add(subject)
        session.commit()
        subject_obj = session.exec(
            select(dbSubject).where(dbSubject.id == subject.id)
        ).first()
        session.close()
    return subject_obj
