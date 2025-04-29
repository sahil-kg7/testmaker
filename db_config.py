from typing import AsyncGenerator
from sqlalchemy import URL
from configparser import ConfigParser
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def __read_config(filename="app_config.ini", section="mysql"):
    config = ConfigParser()
    config.read(filename)
    if config.has_section(section):
        items = dict(config.items(section))
    else:
        raise Exception(f"{section} section not found in file")
    return items


data = __read_config()


def __sql_engine():
    url_obj = URL.create(
        drivername=data["drivername"],
        username=data["username"],
        password=data["password"],
        host=data["host"],
        port=data["port"],
        database=data["database"],
    )
    return create_async_engine(url_obj, echo=True, future=True)


engine = __sql_engine()
# SessionLocal = sessionmaker(class_=Session, autoflush=False, bind=engine)

# Async SessionMaker
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None, None]:
    try:
        async with async_session() as db:
            db.begin()
            yield db
            db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
