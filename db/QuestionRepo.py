# from typing import List
from sqlmodel import Session, select
from sqlalchemy import text
from db_config import sql_engine
from models import Question, toQuestion
from models.dbModels import Mcq, QuestionDetails, toMcq
from typing import List
from typing import List
from typing import List

engine = sql_engine()


async def getQuestionList():
    questions: QuestionDetails
    with Session(engine) as session:
        questions = session.exec(select(QuestionDetails)).all()
        session.close()
    return questions


async def createGeneral(question: Question):
    createdQuestion: Question
    try:
        with Session(engine) as session:
            result = session.exec(
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
            ).first()
            session.commit()
            session.close()
            createdQuestion = toQuestion(result)
        return createdQuestion
    except:
        print("Error occurred in db while creating general question")
        raise


async def createMcq(question: Question):
    createdQuestion: Question
    createdMcqOptions: List[Mcq] = []
    try:
        with Session(engine) as session:
            questionDetailsResult = session.exec(
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
            ).first()
            for option in question.mcq_option:
                res = session.exec(
                    text("CALL create_mcq_option(:questionId, :optionText)"),
                    params={
                        "questionId": questionDetailsResult.id,
                        "optionText": option.option_text,
                    },
                ).first()
                createdMcqOptions.append(toMcq(res))
            session.commit()
            session.close()
            createdQuestion = toQuestion(questionDetailsResult)
            createdQuestion.mcq_option = createdMcqOptions
        return createdQuestion
    except:
        print("Error occurred in db while creating mcq question")
        raise
