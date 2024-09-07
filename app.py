from fastapi import FastAPI

from controllers import (
    ClassController,
    QuestionController,
    SchoolController,
    SubjectController,
    TestController,
)

app = FastAPI()

app.include_router(ClassController.router)
app.include_router(SchoolController.router)
app.include_router(SubjectController.router)
app.include_router(QuestionController.router)
app.include_router(TestController.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
