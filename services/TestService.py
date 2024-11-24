from sqlmodel import Session
from db.TestRepo import TestRepo
from models import TestModel


class TestService:
    def __init__(self, db: Session):
        self.db = db
        self.testRepo = TestRepo(db)

    async def getTestList(self):
        return await self.testRepo.getTestList()

    async def createTest(self, test: TestModel):
        return await self.testRepo.createTest(test)

    async def getTestTypes(self):
        return await self.testRepo.getTestTypes()
