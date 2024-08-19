import uuid
from db import QuestionRepo
from models import Question
from enums.QuestionTypeEnum import QuestionTypeEnum


async def getQuestionList():
    return await QuestionRepo.getQuestionList()


async def createQuestion(question: Question):
    match (QuestionTypeEnum(question.question_type_id).name):
        case QuestionTypeEnum.general.name:
            return await createGeneral(question)
        case QuestionTypeEnum.mcq.name:
            return await createMcq(question)
        case QuestionTypeEnum.fib.name:
            return await createFib(question)
        case QuestionTypeEnum.match.name:
            return await createMatch(question)
        case QuestionTypeEnum.trueFalse.name:
            return await createTrueFalse(question)
        case QuestionTypeEnum.subjective.name:
            return await createSubjective(question)
        case QuestionTypeEnum.reasonAssertion.name:
            return await createReasonAssertion(question)
        case _:
            print("Invalid question type")


async def createGeneral(question: Question):
    try:
        createdQuestion = await QuestionRepo.createGeneral(question)
        return createdQuestion
    except:
        print("Error occurred while creating general question")
        raise


async def createMcq(question: Question):
    try:
        createdQuestion = await QuestionRepo.createMcq(question)
        return createdQuestion
    except:
        print("Error occurred while creating mcq question")


async def createFib(question: Question):
    try:
        print("fib")
    except:
        print("Error occurred while creating fib question")


async def createMatch(question: Question):
    try:
        print("match")
    except:
        print("Error occurred while creating match question")


async def createTrueFalse(question: Question):
    try:
        print("truefalse")
    except:
        print("Error occurred while creating true-false question")


async def createSubjective(question: Question):
    try:
        print("subjective")
    except:
        print("Error occurred while creating subjective question")


async def createReasonAssertion(question: Question):
    try:
        print("reasonassertion")
    except:
        print("Error occurred while creating reason assertion question")
