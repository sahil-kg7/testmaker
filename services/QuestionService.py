import uuid
from db import QuestionRepo
from models import Question
from enums.QuestionTypeEnum import QuestionTypeEnum


async def get_question_list():
    return await QuestionRepo.get_question_list()


async def create_question(question: Question):
    question.id = uuid.uuid4()
    match (QuestionTypeEnum(question.question_type_id).name):
        case QuestionTypeEnum.general.name:
            print("Case general")
        case QuestionTypeEnum.mcq.name:
            print("Case 2")
        case QuestionTypeEnum.fib.name:
            print("Case 3")
        case QuestionTypeEnum.match.name:
            print("Case 4")
        case QuestionTypeEnum.trueFalse.name:
            print("Case 5")
        case QuestionTypeEnum.subjective.name:
            print("Case 6")
        case QuestionTypeEnum.reasonAssertion.name:
            print("Case 7")
        case _:
            print("Invalid question type")
