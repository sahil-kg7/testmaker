from db import TestRepo
from models import TestModel


async def getTestList():
    return await TestRepo.getTestList()


async def createTest(test: TestModel):
    return await TestRepo.createTest(test)


async def getTestTypes():
    return await TestRepo.getTestTypes()
