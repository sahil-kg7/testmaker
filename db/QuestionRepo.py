# from typing import List
from db_config import sql_engine

# from sqlmodel import Session, select
# from models import QuestionDetails

engine = sql_engine()


async def get_question_list():
    print("get_question_list")
    return "get_question_list"
    # with Session(engine) as session:
    #     statement = select(QuestionDetails)
    #     questions = session.exec(statement)
    #     return questions
