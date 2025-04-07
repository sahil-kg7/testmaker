#

from sqlmodel import Session, select
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
    def __init__(self, db: Session):
        self.db = db

    async def getQuestionList(self):
        return self.db.exec(select(QuestionDetails)).all()

    async def getQuestionById(self, questionId: str) -> dbQuestion:
        try:
            question: dbQuestion = self.db.exec(
                select(dbQuestion).where(dbQuestion.id == questionId)
            ).first()
            return question
        except Exception as e:
            print("Error occurred in db while getting question by id.", e.__str__())
            raise

    async def getQuestionsById(self, questionIds: list[str]) -> list[dbQuestion]:
        try:
            questions: list[dbQuestion] = []
            questions = self.db.exec(
                select(dbQuestion).where(dbQuestion.id.in_(questionIds))
            ).all()
            return questions
        except Exception as e:
            print("Error occurred in db while getting questions.", e.__str__())
            raise

    async def getQuestionImages(self, testId: str) -> list[dbQuestionImage]:
        try:
            questionImages: list[dbQuestionImage] = []
            questionImages = self.db.exec(
                select(dbQuestionImage).where(dbQuestionImage.test_id == testId)
            ).all()
            return questionImages
        except Exception as e:
            print("Error occurred in db while getting question images.", e.__str__())
            raise

    async def createGeneral(self, question: Question):
        createdQuestion: Question
        try:
            result = self.db.exec(
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
            createdQuestion = toQuestion(result)
            return createdQuestion
        except Exception as e:
            print("Error occurred in db while creating general question")
            raise

    async def createMcq(self, question: Question):
        createdQuestion: Question
        createdMcqOptions: list[Mcq] = []
        try:
            createdQuestion = await self.createGeneral(question)
            for option in question.mcq_option:
                res = self.db.exec(
                    text("CALL create_mcq_option(:questionId, :optionText)"),
                    params={
                        "questionId": createdQuestion.id,
                        "optionText": option.option_text,
                    },
                ).first()
                createdMcqOptions.append(toMcq(res))
            createdQuestion.mcq_option = createdMcqOptions
            return createdQuestion
        except Exception as e:
            print("Error occurred in db while creating mcq question")
            raise

    async def createFib(self, question: Question):
        createdQuestion: Question
        createdFibWords: list[Fib] = []
        try:
            createdQuestion = await self.createGeneral(question)
            for fib in question.fib_missing_word:
                res = self.db.exec(
                    text("CALL create_fib_missing_word(:questionId, :word)"),
                    params={
                        "questionId": createdQuestion.id,
                        "word": fib.missing_word,
                    },
                ).first()
                createdFibWords.append(toFib(res))
            createdQuestion.fib_missing_word = createdFibWords
            return createdQuestion
        except Exception as e:
            print("Error occurred in db while creating fib question")
            raise

    async def createMatch(self, question: Question):
        createdQuestion: Question
        createdMatchAOptions: list[MatchA] = []
        createdMatchBOptions: list[MatchB] = []
        try:
            createdQuestion = await self.createGeneral(question)
            for a in question.match_a_option:
                res = self.db.exec(
                    text("CALL create_match_a_option(:questionId, :optionText)"),
                    params={
                        "questionId": createdQuestion.id,
                        "optionText": a.match_option,
                    },
                ).first()
                createdMatchAOptions.append(toMatchA(res))
            for b in question.match_b_option:
                res = self.db.exec(
                    text("CALL create_match_b_option(:questionId, :optionText)"),
                    params={
                        "questionId": createdQuestion.id,
                        "optionText": b.match_option,
                    },
                ).first()
                createdMatchBOptions.append(toMatchB(res))
            createdQuestion.match_a_option = createdMatchAOptions
            createdQuestion.match_b_option = createdMatchBOptions
            return createdQuestion
        except Exception as e:
            print("Error occurred in db while creating match question")
            raise

    async def createReasonAssertion(self, question: Question):
        createdQuestion: Question
        createdRA: ReasonAssertion
        try:
            createdQuestion = await self.createGeneral(question)
            res = self.db.exec(
                text(
                    "CALL create_reason_assertion_question(:questionId, :reasonStatement, :assertionStatement)"
                ),
                params={
                    "questionId": createdQuestion.id,
                    "reasonStatement": question.reason_assertion.reason_statement,
                    "assertionStatement": question.reason_assertion.assertion_statement,
                },
            ).first()
            createdRA = toReasonAssertion(res)
            createdQuestion.reason_assertion = createdRA
            return createdQuestion
        except Exception as e:
            print("Error occurred while creating reason-assertion question")
            raise

    async def createQuestionImages(
        self, testId: str, questionImages: list[dbQuestionImage]
    ) -> list[dbQuestionImage]:
        createdQuestionImages: list[dbQuestionImage] = []
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
            return createdQuestionImages
        except Exception as e:
            print("Error occurred in db while creating question images", e.__str__())
            raise
