from db import TestRepo


async def getTestList():
    return await TestRepo.getTestList()


async def createTest(test):
    return await TestRepo.createTest(test)


async def getTestTypes():
    return await TestRepo.getTestTypes()
