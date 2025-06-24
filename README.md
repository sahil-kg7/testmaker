# testmaker
an app to create test papers from the collection of various questions.

this project will enable user to create test papers containing different types of questions such as one word, multiple choice, short answered, fill in the blanks, etc.

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
