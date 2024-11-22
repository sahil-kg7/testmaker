# from typing import List
from fastapi import Depends
from sqlmodel import Session, select
from sqlalchemy import text
from db_config import get_db
from models import Question, toQuestion
from models.dbModels import (
    Fib,
    MatchA,
    MatchB,
    Mcq,
    QuestionDetails,
    ReasonAssertion,
    toMcq,
    toFib,
    toMatchA,
    toMatchB,
    toReasonAssertion,
)
from typing import List
from typing import List
from typing import List


async def getQuestionList(db: Session = Depends(get_db)):
    questions: QuestionDetails
    # with Session(engine) as session:
    #     questions = session.exec(select(QuestionDetails)).all()
    #     session.close()
    # return questions
    questions = db.exec(select(QuestionDetails)).all()
    return questions


# async def createGeneral(question: Question):
#     createdQuestion: Question
#     try:
#         with Session(engine) as session:
#             result = session.exec(
#                 text(
#                     "CALL create_general_question(:questionTypeId, :subjectId, :difficulty, :marks, :content)"
#                 ),
#                 params={
#                     "questionTypeId": question.question_type_id,
#                     "subjectId": question.subject_id,
#                     "difficulty": question.difficulty,
#                     "marks": question.marks,
#                     "content": question.content,
#                 },
#             ).first()
#             session.commit()
#             session.close()
#             createdQuestion = toQuestion(result)
#         return createdQuestion
#     except:
#         print("Error occurred in db while creating general question")
#         raise


# async def createMcq(question: Question):
#     createdQuestion: Question
#     createdMcqOptions: List[Mcq] = []
#     try:
#         createdQuestion = await createGeneral(question)
#         with Session(engine) as session:
#             for option in question.mcq_option:
#                 res = session.exec(
#                     text("CALL create_mcq_option(:questionId, :optionText)"),
#                     params={
#                         "questionId": createdQuestion.id,
#                         "optionText": option.option_text,
#                     },
#                 ).first()
#                 createdMcqOptions.append(toMcq(res))
#             session.commit()
#             session.close()
#             createdQuestion.mcq_option = createdMcqOptions
#         return createdQuestion
#     except:
#         print("Error occurred in db while creating mcq question")
#         raise


# async def createFib(question: Question):
#     createdQuestion: Question
#     createdFibWords: List[Fib] = []
#     try:
#         createdQuestion = await createGeneral(question)
#         with Session(engine) as session:
#             for fib in question.fib_missing_word:
#                 res = session.exec(
#                     text("CALL create_fib_missing_word(:questionId, :word)"),
#                     params={
#                         "questionId": createdQuestion.id,
#                         "word": fib.missing_word,
#                     },
#                 ).first()
#                 createdFibWords.append(toFib(res))
#             session.commit()
#             session.close()
#             createdQuestion.fib_missing_word = createdFibWords
#         return createdQuestion
#     except:
#         print("Error occurred in db while creating fib question")
#         raise


# async def createMatch(question: Question):
#     createdQuestion: Question
#     createdMatchAOptions: List[MatchA] = []
#     createdMatchBOptions: List[MatchB] = []
#     try:
#         createdQuestion = await createGeneral(question)
#         with Session(engine) as session:
#             for a in question.match_a_option:
#                 res = session.exec(
#                     text("CALL create_match_a_option(:questionId, :optionText)"),
#                     params={
#                         "questionId": createdQuestion.id,
#                         "optionText": a.match_option,
#                     },
#                 ).first()
#                 createdMatchAOptions.append(toMatchA(res))
#             for b in question.match_b_option:
#                 res = session.exec(
#                     text("CALL create_match_b_option(:questionId, :optionText)"),
#                     params={
#                         "questionId": createdQuestion.id,
#                         "optionText": b.match_option,
#                     },
#                 ).first()
#                 createdMatchBOptions.append(toMatchB(res))
#             session.commit()
#             session.close()
#             createdQuestion.match_a_option = createdMatchAOptions
#             createdQuestion.match_b_option = createdMatchBOptions
#         return createdQuestion
#     except:
#         print("Error occurred in db while creating match question")
#         raise


# async def createReasonAssertion(question: Question):
#     createdQuestion: Question
#     createdRA: ReasonAssertion
#     try:
#         createdQuestion = await createGeneral(question)
#         with Session(engine) as session:
#             res = session.exec(
#                 text(
#                     "CALL create_reason_assertion_question(:questionId, :reasonStatement, :assertionStatement)"
#                 ),
#                 params={
#                     "questionId": createdQuestion.id,
#                     "reasonStatement": question.reason_assertion.reason_statement,
#                     "assertionStatement": question.reason_assertion.assertion_statement,
#                 },
#             ).first()
#             session.commit()
#             session.close()
#             createdRA = toReasonAssertion(res)
#             createdQuestion.reason_assertion = createdRA
#         return createdQuestion
#     except:
#         print("Error occurred while creating reason-assertion question")
#         raise
