from typing import List
from models.dbModels import School as dbSchool
from db import SchoolRepo


async def get_school_list():
    schoolList: List[dbSchool] = await SchoolRepo.get_school_list()
    return schoolList


async def create_school(school: dbSchool):
    return await SchoolRepo.create_school(school)
