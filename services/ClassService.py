from typing import List
from models.dbModels import Class as dbClass
from db import ClassRepo


async def get_class_list():
    classList: List[dbClass] = await ClassRepo.get_class_list()
    return classList


async def create_class(class_: dbClass):
    return await ClassRepo.create_class(class_)
