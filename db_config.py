from typing import Generator
from sqlalchemy import URL, create_engine
from configparser import ConfigParser
from sqlmodel import Session

# from sqlalchemy.orm import sessionmaker


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
        query={"unix_socket": "/var/snap/mysql/current/run/mysqld.sock"},
    )
    return create_engine(url_obj)


engine = __sql_engine()
# SessionLocal = sessionmaker(class_=Session, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    try:
        with Session(engine) as db:
            db.begin()
            yield db
            db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
