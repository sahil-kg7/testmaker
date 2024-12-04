from sqlalchemy import text
from sqlmodel import Session, select
from models import TestModel, toTestModelFromDbTest
from models.dbModels import (
    QuestionDetails as dbQuestion,
    QuestionImages as dbQuestionImage,
    QuestionSubquestionMap as dbQuesSubquesMap,
    Test as dbTest,
    TestQuestionMap as dbTestQuesMap,
    TestSectionMap as dbTestSectionMap,
    TestType as dbTestType,
    toTest,
    toTestQuestionMap,
    toQuestionSubquestionMap,
    toTestSectionMap,
    toQuestionImages,
    toQuestionDetails,
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
            for test in tests:
                test.questions = []
                test.question_map = self.db.exec(
                    select(dbTestQuesMap).where(dbTestQuesMap.test_id == test.id)
                ).all()
                test.questions.extend(
                    [
                        toQuestionDetails(ques)
                        for ques in self.db.exec(
                            select(dbQuestion).where(
                                dbQuestion.id.in_(
                                    [
                                        quesMap.question_id
                                        for quesMap in test.question_map
                                    ]
                                )
                            )
                        ).all()
                    ]
                )
                test.subquestion_map = self.db.exec(
                    select(dbQuesSubquesMap).where(dbQuesSubquesMap.test_id == test.id)
                ).all()
                test.questions.extend(
                    [
                        toQuestionDetails(subques)
                        for subques in self.db.exec(
                            select(dbQuestion).where(
                                dbQuestion.id.in_(
                                    [
                                        subquesMap.subquestion_id
                                        for subquesMap in test.subquestion_map
                                    ]
                                )
                            )
                        )
                    ]
                )
                test.section_map = self.db.exec(
                    select(dbTestSectionMap).where(dbTestSectionMap.test_id == test.id)
                ).all()
            return tests
        except Exception as e:
            print("Error occurred in db while getting test list.", e.__str__())
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

    async def createQuestionImages(
        self, testId: str, questionImages: list[dbQuestionImage]
    ) -> list[dbQuestionImage]:
        createdQuestionImages: list[dbQuestionImage] = []
        try:
            for image in questionImages:
                res = self.db.exec(
                    text(
                        "CALL create_question_images(:testId, :questionId, :imagePosition, :imageName)"
                    ),
                    params={
                        "testId": testId,
                        "questionId": image.question_id,
                        "imagePosition": image.image_position,
                        "imageName": image.image_name,
                    },
                ).first()
                createdQuestionImages.append(toQuestionImages(res))
            return createdQuestionImages
        except Exception as e:
            print("Error occurred in db while creating question images", e.__str__())
            raise
