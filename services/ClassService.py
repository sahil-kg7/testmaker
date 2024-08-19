from typing import List
from models.dbModels import Class as dbClass
from db import ClassRepo


async def getClassList():
    classList: List[dbClass] = await ClassRepo.getClassList()
    return classList


async def createClass(class_: dbClass):
    return await ClassRepo.createClass(class_)
