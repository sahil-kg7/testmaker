from sqlmodel import Session
from db.TestRepo import TestRepo
from models import TestModel, toTestModel
from models.dbModels import TestType as dbTestType


class TestService:
    def __init__(self, db: Session):
        self.db = db
        self.testRepo = TestRepo(db)

    async def getTestList(self, page: int):
        return await self.testRepo.getTestList(page)

    async def getTestTypes(self) -> list[dbTestType]:
        return await self.testRepo.getTestTypes()

    async def createTest(self, test: TestModel) -> TestModel:
        createdTest: TestModel
        testDetails = await self.testRepo.createTest(test)
        createdTest = toTestModel(testDetails)
        createdTestQuesMap = await self.testRepo.createTestQuestionMap(
            testDetails.id, test.question_map
        )
        createdQuesSubquesMap = await self.testRepo.createQuesSubquesMap(
            testDetails.id, test.subquestion_map
        )
        createdTestSectionMap = await self.testRepo.createTestSectionMap(
            testDetails.id, test.section_map
        )
        createdQuestionImages = await self.testRepo.createQuestionImages(
            testDetails.id, test.question_images
        )
        createdTest.question_map = createdTestQuesMap
        createdTest.subquestion_map = createdQuesSubquesMap
        createdTest.section_map = createdTestSectionMap
        createdTest.question_images = createdQuestionImages
        return createdTest
