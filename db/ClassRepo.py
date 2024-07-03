from typing import List
from db_config import sql_engine
from sqlmodel import Session, select
from models.dbModels import Class as dbClass

engine = sql_engine()


async def get_class_list():
    classList: List[dbClass] = []
    with Session(engine) as session:
        classList = session.exec(select(dbClass)).all()
        session.close()
    return classList


async def create_class(class_: dbClass) -> dbClass:
    class_obj = dbClass
    with Session(engine) as session:
        session.add(class_)
        session.commit()
        class_obj = session.exec(
            select(dbClass).where(dbClass.class_number == class_.class_number)
        ).first()
        session.close()
    return class_obj
