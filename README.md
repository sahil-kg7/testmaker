# testmaker
This project allows users to create customizable test papers from a collection of questions, supporting multiple formats such as one-word answers, multiple choice, short answers, and fill-in-the-blanks.

Steps to initiate the project with uv:

 - uv init
 - uv venv
 - source .venv/bin/activate
 - uv pip install -r requirements.txt (installs all packages from requirements.txt)


to enable virtual environment:
`source .venv/bin/activate`

to disable the virtual environment:
`deactivate` or `source deactivate`

install following packages from pip:
`fastapi`, `sqlmodel`, `pydantic` (not required if `sqlmodel` installed), `SQLAlchemy` (not required if `sqlmodel` installed), `mysqlclient`, `mysql-connector-python`
