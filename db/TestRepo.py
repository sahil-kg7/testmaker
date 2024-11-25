from typing import List

from sqlalchemy import text
from sqlmodel import Session, select
from models import TestModel
from models.dbModels import (
    QuestionImages as dbQuestionImages,
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
)


class TestRepo:
    def __init__(self, db: Session):
        self.db = db

    async def getTestList(self):
        tests: List[TestModel] = []
        tests = self.db.exec(select(dbTest)).all()
        for test in tests:
            test.question_map = self.db.exec(
                select(dbTestQuesMap).where(dbTestQuesMap.id == test.id)
            ).first()
        return tests

    async def getTestTypes(self) -> List[dbTestType]:
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
            self.db.expire()
            createdTest = toTest(res)
            return createdTest
        except:
            print("Error occurred in db while creating test")
            raise

    async def createTestQuestionMap(
        self, testId: str, quesMap: List[dbTestQuesMap]
    ) -> List[dbTestQuesMap]:
        createdTestQuestionMap: List[dbTestQuesMap] = []
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
        except:
            print("Error occurred in db while creating test question map")
            raise

    async def createQuesSubquesMap(
        self, testId: str, subquesMap: List[dbQuesSubquesMap]
    ) -> List[dbQuesSubquesMap]:
        createdQuesSubquesMap: List[dbQuesSubquesMap] = []
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
        except:
            print("Error occurred in db while creating question subquestion map")
            raise

    async def createTestSectionMap(
        self, testId: str, sectionMap: List[dbTestSectionMap]
    ) -> List[dbTestSectionMap]:
        createdTestSectionMap: List[dbTestSectionMap] = []
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
        except:
            print("Error occurred in db while creating test section map")
            raise

    async def createQuestionImages(
        self, testId: str, questionImages: List[dbQuestionImages]
    ) -> List[dbQuestionImages]:
        createdQuestionImages: List[dbQuestionImages] = []
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
            return
        except:
            print("Error occurred in db while creating question images")
            raise
