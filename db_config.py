from sqlalchemy import URL, create_engine
from configparser import ConfigParser


def read_config(filename="app_config.ini", section="mysql"):
    config = ConfigParser()
    config.read(filename)
    if config.has_section(section):
        items = dict(config.items(section))
    else:
        raise Exception(f"{section} section not found in file")
    return items


data = read_config()


def sql_engine():
    url_obj = URL.create(
        drivername=data["drivername"],
        username=data["username"],
        password=data["password"],
        host=data["host"],
        port=data["port"],
        database=data["database"],
    )
    return create_engine(url_obj)
