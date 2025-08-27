from typing import Optional
from utils import LogUtil
from exceptions import AppException, DatabaseException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import text
from models import Question, toQuestion
from models.dbModels import (
    Fib,
    MatchA,
    MatchB,
    Mcq,
    QuestionDetails,
    ReasonAssertion,
    QuestionDetails as dbQuestion,
    QuestionImages as dbQuestionImage,
    toMcq,
    toFib,
    toMatchA,
    toMatchB,
    toReasonAssertion,
    toQuestionImages,
)


class QuestionRepo:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.logger = LogUtil(__name__)

    async def getQuestionList(self):
        try:
            statement = select(dbQuestion)
            result = await self.db.exec(statement)
            questions = result.all()
            return questions
        except Exception as e:
            self.logger.error(
                f"Failed to fetch question list: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to fetch question list", original_exception=e
            ) from e

    async def getQuestionById(self, questionId: str) -> Optional[dbQuestion]:
        try:
            statement = select(dbQuestion).where(dbQuestion.id == questionId)
            result = await self.db.exec(statement)
            question = result.first()
            return question
        except Exception as e:
            self.logger.error(
                f"Failed to fetch question with ID {questionId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch question with ID {questionId}",
                original_exception=e,
            ) from e

    async def getQuestionsById(self, questionIds: list[str]) -> list[dbQuestion]:
        try:
            statement = select(dbQuestion).where(dbQuestion.id.in_(questionIds))
            result = await self.db.exec(statement)
            questions = result.all()
            return questions
        except Exception as e:
            self.logger.error(
                f"Failed to fetch questions with IDs {questionIds}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch questions with IDs {questionIds}",
                original_exception=e,
            ) from e

    async def getQuestionImages(self, testId: str) -> list[dbQuestionImage]:
        try:
            statement = select(dbQuestionImage).where(dbQuestionImage.test_id == testId)
            result = await self.db.exec(statement)
            questionImages = result.all()
            return questionImages
        except Exception as e:
            self.logger.error(
                f"Failed to fetch question images for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to fetch question images for test ID {testId}",
                original_exception=e,
            ) from e

    async def createGeneral(self, question: Question):
        try:
            result = await self.db.exec(
                text(
                    "CALL create_general_question(:questionTypeId, :subjectId, :difficulty, :marks, :content)"
                ),
                params={
                    "questionTypeId": question.question_type_id,
                    "subjectId": question.subject_id,
                    "difficulty": question.difficulty,
                    "marks": question.marks,
                    "content": question.content,
                },
            )
            createdQuestion = toQuestion(result.first())
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create general question: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create general question",
                original_exception=e,
            ) from e

    async def createMcq(self, question: Question):
        try:
            createdQuestion = await self.createGeneral(question)
            createdMcqOptions: list[Mcq] = []
            for option in question.mcq_option:
                result = await self.db.exec(
                    text("CALL create_mcq_option(:questionId, :optionText)"),
                    params={
                        "questionId": createdQuestion.id,
                        "optionText": option.option_text,
                    },
                )
                createdMcqOptions.append(toMcq(result.first()))
            createdQuestion.mcq_option = createdMcqOptions
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create MCQ question: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create MCQ question",
                original_exception=e,
            ) from e

    async def createFib(self, question: Question):
        try:
            createdQuestion = await self.createGeneral(question)
            createdFibWords: list[Fib] = []
            for fib in question.fib_missing_word:
                result = await self.db.exec(
                    text("CALL create_fib_missing_word(:questionId, :word)"),
                    params={
                        "questionId": createdQuestion.id,
                        "word": fib.missing_word,
                    },
                )
                createdFibWords.append(toFib(result.first()))
            createdQuestion.fib_missing_word = createdFibWords
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create FIB question: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create FIB question",
                original_exception=e,
            ) from e

    async def createMatch(self, question: Question):
        try:
            createdQuestion = await self.createGeneral(question)
            createdMatchAOptions: list[MatchA] = []
            createdMatchBOptions: list[MatchB] = []
            for a in question.match_a_option:
                result = await self.db.exec(
                    text("CALL create_match_a_option(:questionId, :optionText)"),
                    params={
                        "questionId": createdQuestion.id,
                        "optionText": a.match_option,
                    },
                )
                createdMatchAOptions.append(toMatchA(result.first()))
            for b in question.match_b_option:
                result = await self.db.exec(
                    text("CALL create_match_b_option(:questionId, :optionText)"),
                    params={
                        "questionId": createdQuestion.id,
                        "optionText": b.match_option,
                    },
                )
                createdMatchBOptions.append(toMatchB(result.first()))
            createdQuestion.match_a_option = createdMatchAOptions
            createdQuestion.match_b_option = createdMatchBOptions
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create match question: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create match question",
                original_exception=e,
            ) from e

    async def createReasonAssertion(self, question: Question):
        try:
            createdQuestion = await self.createGeneral(question)
            result = await self.db.exec(
                text(
                    "CALL create_reason_assertion_question(:questionId, :reasonStatement, :assertionStatement)"
                ),
                params={
                    "questionId": createdQuestion.id,
                    "reasonStatement": question.reason_assertion.reason_statement,
                    "assertionStatement": question.reason_assertion.assertion_statement,
                },
            )
            createdRA = toReasonAssertion(result.first())
            createdQuestion.reason_assertion = createdRA
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create reason-assertion question: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                "Failed to create reason-assertion question",
                original_exception=e,
            ) from e

    async def createQuestionImages(
        self, testId: str, questionImages: list[dbQuestionImage]
    ) -> list[dbQuestionImage]:
        try:
            createdQuestionImages: list[dbQuestionImage] = []
            for image in questionImages:
                result = await self.db.exec(
                    text(
                        "CALL create_question_images(:testId, :questionId, :imagePosition, :imageName)"
                    ),
                    params={
                        "testId": testId,
                        "questionId": image.question_id,
                        "imagePosition": image.image_position,
                        "imageName": image.image_name,
                    },
                )
                createdQuestionImages.append(toQuestionImages(result.first()))
            return createdQuestionImages
        except Exception as e:
            self.logger.error(
                f"Failed to create question images for test ID {testId}: {e.__str__()}",
                exc_info=True,
            )
            raise DatabaseException(
                f"Failed to create question images for test ID {testId}",
                original_exception=e,
            ) from e
