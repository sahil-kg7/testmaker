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


class TestRepo:
    # default page size is 10
    def __init__(self, db: Session):
        self.db = db
        self.pageSize = 10

    async def getTestList(self, page: int):
        try:
            tests: list[TestModel] = []
            testRes = self.db.exec(
                select(dbTest).order_by(dbTest.created_on).offset(page * self.pageSize)
            ).all()
            tests = [toTestModelFromDbTest(test) for test in testRes]
            return tests
        except Exception as e:
            print("Error occurred in db while getting test list.", e.__str__())
            raise

    async def getTestQuestionMap(self, testId: str) -> list[dbTestQuesMap]:
        try:
            testQuestionMap: list[dbTestQuesMap] = []
            testQuestionMap = self.db.exec(
                select(dbTestQuesMap).where(dbTestQuesMap.test_id == testId)
            ).all()
            return testQuestionMap
        except Exception as e:
            print("Error occurred in db while getting test question map.", e.__str__())
            raise

    async def getSubquestionMap(self, testId: str) -> list[dbQuesSubquesMap]:
        try:
            subquestionMap: list[dbQuesSubquesMap] = []
            subquestionMap = self.db.exec(
                select(dbQuesSubquesMap).where(dbQuesSubquesMap.test_id == testId)
            ).all()
            return subquestionMap
        except Exception as e:
            print("Error occurred in db while getting subquestion map.", e.__str__())
            raise

    async def getSectionMap(self, testId: str) -> list[dbTestSectionMap]:
        try:
            sectionMap: list[dbTestSectionMap] = []
            sectionMap = self.db.exec(
                select(dbTestSectionMap).where(dbTestSectionMap.test_id == testId)
            ).all()
            return sectionMap
        except Exception as e:
            print("Error occurred in db while getting section map.", e.__str__())
            raise

    async def getTestTypes(self) -> list[dbTestType]:
        return self.db.exec(select(dbTestType)).all()

    async def createTest(self, test: dbTest) -> dbTest:
        createdTest: dbTest
        try:
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
            print("Error occurred in db while creating test.", e.__str__())
            raise

    async def createTestQuestionMap(
        self, testId: str, quesMap: list[dbTestQuesMap]
    ) -> list[dbTestQuesMap]:
        createdTestQuestionMap: list[dbTestQuesMap] = []
        try:
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
            print("Error occurred in db while creating test question map.", e.__str__())
            raise

    async def createQuesSubquesMap(
        self, testId: str, subquesMap: list[dbQuesSubquesMap]
    ) -> list[dbQuesSubquesMap]:
        createdQuesSubquesMap: list[dbQuesSubquesMap] = []
        try:
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
            print(
                "Error occurred in db while creating question subquestion map",
                e.__str__(),
            )
            raise

    async def createTestSectionMap(
        self, testId: str, sectionMap: list[dbTestSectionMap]
    ) -> list[dbTestSectionMap]:
        createdTestSectionMap: list[dbTestSectionMap] = []
        try:
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
            print("Error occurred in db while creating test section map", e.__str__())
            raise
