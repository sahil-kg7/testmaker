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
        raise


async def createFib(question: Question):
    try:
        createdQuestion = await QuestionRepo.createFib(question)
        return createdQuestion
    except:
        print("Error occurred while creating fib question")
        raise


async def createMatch(question: Question):
    try:
        createdQuestion = await QuestionRepo.createMatch(question)
        return createdQuestion
    except:
        print("Error occurred while creating match question")
        raise


async def createTrueFalse(question: Question):
    try:
        ## only question type will be set to true/false
        createdQuestion = await QuestionRepo.createGeneral(question)
        return createdQuestion
    except:
        print("Error occurred while creating true-false question")
        raise


async def createSubjective(question: Question):
    try:
        ## only question type will be set to subjective
        createdQuestion = await QuestionRepo.createGeneral(question)
        return createdQuestion
    except:
        print("Error occurred while creating subjective question")
        raise


async def createReasonAssertion(question: Question):
    try:
        createdQuestion = await QuestionRepo.createReasonAssertion(question)
        return createdQuestion
    except:
        print("Error occurred while creating reason assertion question")
        raise
