from sqlmodel import Session
from db.QuestionRepo import QuestionRepo
from models import Question
from enums.QuestionTypeEnum import QuestionTypeEnum
from utils import LogUtil
from exceptions import AppException


class QuestionService:

    def __init__(self, db: Session):
        self.db = db
        self.questionRepo: QuestionRepo = QuestionRepo(db)
        self.logger = LogUtil(__name__)

    async def getQuestionList(self):
        try:
            return await self.questionRepo.getQuestionList()
        except Exception as e:
            self.logger.error(
                f"Failed to get question list: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to get question list",
                original_exception=e,
            ) from e

    async def createQuestion(self, question: Question):
        try:
            match (QuestionTypeEnum(question.question_type_id).name):
                case QuestionTypeEnum.general.name:
                    return await self.createGeneral(question)
                case QuestionTypeEnum.mcq.name:
                    return await self.createMcq(question)
                case QuestionTypeEnum.fib.name:
                    return await self.createFib(question)
                case QuestionTypeEnum.match.name:
                    return await self.createMatch(question)
                case QuestionTypeEnum.trueFalse.name:
                    return await self.createTrueFalse(question)
                case QuestionTypeEnum.subjective.name:
                    return await self.createSubjective(question)
                case QuestionTypeEnum.reasonAssertion.name:
                    return await self.createReasonAssertion(question)
                case _:
                    self.logger.error(
                        f"Invalid question type: {question.question_type_id}",
                        exc_info=True,
                    )
                    raise AppException(
                        f"Invalid question type: {question.question_type_id}"
                    )
        except Exception as e:
            self.logger.error(
                f"Failed to create question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create question",
                original_exception=e,
            ) from e

    async def createGeneral(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createGeneral(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create general question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create general question",
                original_exception=e,
            ) from e

    async def createMcq(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createMcq(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create MCQ question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create MCQ question",
                original_exception=e,
            ) from e

    async def createFib(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createFib(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create FIB question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create FIB question",
                original_exception=e,
            ) from e

    async def createMatch(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createMatch(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create match question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create match question",
                original_exception=e,
            ) from e

    async def createTrueFalse(self, question: Question):
        try:
            ## only question type will be set to true/false
            createdQuestion = await self.questionRepo.createGeneral(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create true-false question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create true-false question",
                original_exception=e,
            ) from e

    async def createSubjective(self, question: Question):
        try:
            ## only question type will be set to subjective
            createdQuestion = await self.questionRepo.createGeneral(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create subjective question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create subjective question",
                original_exception=e,
            ) from e

    async def createReasonAssertion(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createReasonAssertion(question)
            return createdQuestion
        except Exception as e:
            self.logger.error(
                f"Failed to create reason assertion question: {e.__str__()}",
                exc_info=True,
            )
            raise AppException(
                "Failed to create reason assertion question",
                original_exception=e,
            ) from e
