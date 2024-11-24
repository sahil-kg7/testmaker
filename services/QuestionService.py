from sqlmodel import Session
from db.QuestionRepo import QuestionRepo
from models import Question
from enums.QuestionTypeEnum import QuestionTypeEnum


class QuestionService:

    def __init__(self, db: Session):
        self.db = db
        self.questionRepo: QuestionRepo = QuestionRepo(db)

    async def getQuestionList(self):
        return await self.questionRepo.getQuestionList()

    async def createQuestion(self, question: Question):
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
                print("Invalid question type")

    async def createGeneral(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createGeneral(question)
            return createdQuestion
        except:
            print("Error occurred while creating general question")
            raise

    async def createMcq(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createMcq(question)
            return createdQuestion
        except:
            print("Error occurred while creating mcq question")
            raise

    async def createFib(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createFib(question)
            return createdQuestion
        except:
            print("Error occurred while creating fib question")
            raise

    async def createMatch(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createMatch(question)
            return createdQuestion
        except:
            print("Error occurred while creating match question")
            raise

    async def createTrueFalse(self, question: Question):
        try:
            ## only question type will be set to true/false
            createdQuestion = await self.questionRepo.createGeneral(question)
            return createdQuestion
        except:
            print("Error occurred while creating true-false question")
            raise

    async def createSubjective(self, question: Question):
        try:
            ## only question type will be set to subjective
            createdQuestion = await self.questionRepo.createGeneral(question)
            return createdQuestion
        except:
            print("Error occurred while creating subjective question")
            raise

    async def createReasonAssertion(self, question: Question):
        try:
            createdQuestion = await self.questionRepo.createReasonAssertion(question)
            return createdQuestion
        except:
            print("Error occurred while creating reason assertion question")
            raise
