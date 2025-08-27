from sqlmodel import Session
from db.QuestionRepo import QuestionRepo
from db.TestRepo import TestRepo
from models import TestModel, toTestModelFromDbTest
from models.dbModels import TestType as dbTestType, toQuestionDetails
from utils import LogUtil
from exceptions import AppException


class TestService:
    def __init__(self, db: Session):
        self.db = db
        self.testRepo = TestRepo(db)
        self.questionRepo = QuestionRepo(db)
        self.logger = LogUtil(__name__)

    async def getTestList(self, page: int):
        try:
            tests = await self.testRepo.getTestList(page)
            for test in tests:
                test.questions = []
                test.question_map = await self.testRepo.getTestQuestionMap(test.id)
                test.questions.extend(
                    [
                        toQuestionDetails(ques)
                        for ques in await self.questionRepo.getQuestionsById(
                            [quesMap.question_id for quesMap in test.question_map]
                        )
                    ]
                )
                test.subquestion_map = await self.testRepo.getSubquestionMap(test.id)
                test.questions.extend(
                    [
                        toQuestionDetails(ques)
                        for ques in await self.questionRepo.getQuestionsById(
                            [quesMap.subquestion_id for quesMap in test.subquestion_map]
                        )
                    ]
                )
                test.section_map = await self.testRepo.getSectionMap(test.id)
                for question in test.questions:
                    test.question_images = []
                    test.question_images.extend(
                        [
                            image
                            for image in await self.questionRepo.getQuestionImages(
                                question.id
                            )
                        ]
                    )
            return tests
        except Exception as e:
            self.logger.error(
                f"Failed to get test list for page {page}: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                f"Failed to get test list for page {page}",
                original_exception=e,
            ) from e

    async def getTestTypes(self) -> list[dbTestType]:
        try:
            return await self.testRepo.getTestTypes()
        except Exception as e:
            self.logger.error(
                f"Failed to get test types: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to get test types",
                original_exception=e,
            ) from e

    async def createTest(self, test: TestModel) -> TestModel:
        try:
            createdTest: TestModel
            testDetails = await self.testRepo.createTest(test)
            createdTest = toTestModelFromDbTest(testDetails)
            createdTestQuesMap = await self.testRepo.createTestQuestionMap(
                testDetails.id, test.question_map
            )
            createdQuesSubquesMap = await self.testRepo.createQuesSubquesMap(
                testDetails.id, test.subquestion_map
            )
            createdTestSectionMap = await self.testRepo.createTestSectionMap(
                testDetails.id, test.section_map
            )
            # TODO: repo layer to be implemented
            # createdQuestionImages = await self.testRepo.createQuestionImages(
            #     testDetails.id, test.question_images
            # )
            createdTest.question_map = createdTestQuesMap
            createdTest.subquestion_map = createdQuesSubquesMap
            createdTest.section_map = createdTestSectionMap
            # createdTest.question_images = createdQuestionImages
            return createdTest
        except Exception as e:
            self.logger.error(
                f"Failed to create test: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create test",
                original_exception=e,
            ) from e
