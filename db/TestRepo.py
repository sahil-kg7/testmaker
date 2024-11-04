from typing import List

from sqlmodel import Session, select
from db_config import sql_engine
from models import TestModel
from models.dbModels import Test, TestQuestionMap, TestType as dbTestType


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


async def getTestTypes():
    test_types: List[dbTestType] = []
    with Session(engine) as session:
        test_types = session.exec(select(dbTestType)).all()
        session.close()
    return test_types
