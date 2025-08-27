from sqlalchemy import text
from sqlmodel import Session, select
from models import TestModel, toTestModelFromDbTest
from models.dbModels import (
    QuestionSubquestionMap as dbQuesSubquesMap,
    Test as dbTest,
    TestQuestionMap as dbTestQuesMap,
    TestSectionMap as dbTestSectionMap,
    TestType as dbTestType,
    toTest,
    toTestQuestionMap,
    toQuestionSubquestionMap,
    toTestSectionMap,
)
from utils import LogUtil
from exceptions import DatabaseException


class TestRepo:
    # default page size is 10
    def __init__(self, db: Session):
        self.db = db
        self.pageSize = 10
        self.logger = LogUtil(__name__)

    async def getTestList(self, page: int):
        try:
            tests: list[TestModel] = []
            testRes = self.db.exec(
                select(dbTest).order_by(dbTest.created_on).offset(page * self.pageSize)
            ).all()
            tests = [toTestModelFromDbTest(test) for test in testRes]
            return tests
        except Exception as e:
            self.logger.error(
                f"Failed to fetch test list for page {page}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch test list for page {page}",
                original_exception=e,
            ) from e

    async def getTestQuestionMap(self, testId: str) -> list[dbTestQuesMap]:
        try:
            testQuestionMap: list[dbTestQuesMap] = []
            testQuestionMap = self.db.exec(
                select(dbTestQuesMap).where(dbTestQuesMap.test_id == testId)
            ).all()
            return testQuestionMap
        except Exception as e:
            self.logger.error(
                f"Failed to fetch test question map for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch test question map for test ID {testId}",
                original_exception=e,
            ) from e

    async def getSubquestionMap(self, testId: str) -> list[dbQuesSubquesMap]:
        try:
            subquestionMap: list[dbQuesSubquesMap] = []
            subquestionMap = self.db.exec(
                select(dbQuesSubquesMap).where(dbQuesSubquesMap.test_id == testId)
            ).all()
            return subquestionMap
        except Exception as e:
            self.logger.error(
                f"Failed to fetch subquestion map for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch subquestion map for test ID {testId}",
                original_exception=e,
            ) from e

    async def getSectionMap(self, testId: str) -> list[dbTestSectionMap]:
        try:
            sectionMap: list[dbTestSectionMap] = []
            sectionMap = self.db.exec(
                select(dbTestSectionMap).where(dbTestSectionMap.test_id == testId)
            ).all()
            return sectionMap
        except Exception as e:
            self.logger.error(
                f"Failed to fetch section map for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch section map for test ID {testId}",
                original_exception=e,
            ) from e

    async def getTestTypes(self) -> list[dbTestType]:
        try:
            statement = select(dbTestType)
            result = self.db.exec(statement)
            testTypes = result.all()
            return testTypes
        except Exception as e:
            self.logger.error(
                f"Failed to fetch test types: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to fetch test types", original_exception=e
            ) from e

    async def createTest(self, test: dbTest) -> dbTest:
        try:
            createdTest: dbTest
            res = self.db.exec(
                text(
                    "CALL create_test(:fileName, :schoolId, :classNumber, :subjectId, :testTypeId, :sectionCount, :timeDuration, :maximumMarks)"
                ),
                params={
                    "fileName": test.file_name,
                    "schoolId": test.school_id,
                    "classNumber": test.class_number,
                    "subjectId": test.subject_id,
                    "testTypeId": test.test_type_id,
                    "sectionCount": test.section_count,
                    "timeDuration": test.time_duration,
                    "maximumMarks": test.maximum_marks,
                },
            ).first()
            self.db.expire_all()
            createdTest = toTest(res)
            return createdTest
        except Exception as e:
            self.logger.error(
                f"Failed to create test: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create test", original_exception=e
            ) from e

    async def createTestQuestionMap(
        self, testId: str, quesMap: list[dbTestQuesMap]
    ) -> list[dbTestQuesMap]:
        try:
            createdTestQuestionMap: list[dbTestQuesMap] = []
            for ques in quesMap:
                res = self.db.exec(
                    text(
                        "CALL create_test_question_map(:testId, :questionId, :questionPosition)"
                    ),
                    params={
                        "testId": testId,
                        "questionId": ques.question_id,
                        "questionPosition": ques.question_position,
                    },
                ).first()
                createdTestQuestionMap.append(toTestQuestionMap(res))
            return createdTestQuestionMap
        except Exception as e:
            self.logger.error(
                f"Failed to create test question map for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to create test question map for test ID {testId}",
                original_exception=e,
            ) from e

    async def createQuesSubquesMap(
        self, testId: str, subquesMap: list[dbQuesSubquesMap]
    ) -> list[dbQuesSubquesMap]:
        try:
            createdQuesSubquesMap: list[dbQuesSubquesMap] = []
            for subques in subquesMap:
                res = self.db.exec(
                    text(
                        "CALL create_question_subquestion_map(:testId, :questionId, :subquestionId, :subquestionNumber)"
                    ),
                    params={
                        "testId": testId,
                        "questionId": subques.question_id,
                        "subquestionId": subques.subquestion_id,
                        "subquestionNumber": subques.subquestion_number,
                    },
                ).first()
                createdQuesSubquesMap.append(toQuestionSubquestionMap(res))
            return createdQuesSubquesMap
        except Exception as e:
            self.logger.error(
                f"Failed to create question subquestion map for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to create question subquestion map for test ID {testId}",
                original_exception=e,
            ) from e

    async def createTestSectionMap(
        self, testId: str, sectionMap: list[dbTestSectionMap]
    ) -> list[dbTestSectionMap]:
        try:
            createdTestSectionMap: list[dbTestSectionMap] = []
            for section in sectionMap:
                res = self.db.exec(
                    text(
                        "CALL create_test_section_map(:testId, :sectionNumber, :initialQuesNumber)"
                    ),
                    params={
                        "testId": testId,
                        "sectionNumber": section.section_number,
                        "initialQuesNumber": section.initial_ques_number,
                    },
                ).first()
                createdTestSectionMap.append(toTestSectionMap(res))
            return createdTestSectionMap
        except Exception as e:
            self.logger.error(
                f"Failed to create test section map for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to create test section map for test ID {testId}",
                original_exception=e,
            ) from e
