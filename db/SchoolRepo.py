from typing import List
from db_config import sql_engine
from sqlmodel import Session, select
from models.dbModels import School as dbSchool

engine = sql_engine()


async def get_school_list():
    schoolList: List[dbSchool] = []
    with Session(engine) as session:
        schoolList = session.exec(select(dbSchool)).all()
        session.close()
    return schoolList


async def create_school(school: dbSchool) -> dbSchool:
    school_obj = dbSchool()
    with Session(engine) as session:
        session.add(school)
        session.commit()
        school_obj = session.exec(
            select(dbSchool).where(dbSchool.id == school.id)
        ).first()
        session.close()
    return school_obj
