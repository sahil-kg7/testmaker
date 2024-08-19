from typing import List
from models.dbModels import School as dbSchool
from db import SchoolRepo


async def getSchoolList():
    schoolList: List[dbSchool] = await SchoolRepo.getSchoolList()
    return schoolList


async def createSchool(school: dbSchool):
    return await SchoolRepo.createSchool(school)
