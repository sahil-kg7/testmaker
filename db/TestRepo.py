from typing import List

from sqlmodel import Session, select
from db_config import sql_engine
from models import TestModel
from models.dbModels import Test, TestQuestionMap


engine = sql_engine()


async def getTestList():
    tests: List[TestModel] = []
    with Session(engine) as session:
        tests = session.exec(select(Test)).all()
        for test in tests:
            test.question_map = session.exec(
                select(TestQuestionMap).where(TestQuestionMap.id == test.id)
            ).first()
        session.close()
    return tests
