from typing import List

from sqlmodel import Session, select
from models import TestModel
from models.dbModels import Test, TestQuestionMap, TestType as dbTestType


class TestRepo:
    def __init__(self, db: Session):
        self.db = db

    async def getTestList(self):
        tests: List[TestModel] = []
        tests = self.db.exec(select(Test)).all()
        for test in tests:
            test.question_map = self.db.exec(
                select(TestQuestionMap).where(TestQuestionMap.id == test.id)
            ).first()
        return tests

    async def getTestTypes(self):
        return self.db.exec(select(dbTestType)).all()

    async def createTest(self, test: TestModel) -> TestModel:
        created_test: TestModel
        self.db.add(test)
        self.db.expire()
        test_obj = self.db.exec(select(Test).where(Test.id == test.id)).first()
        return test_obj
