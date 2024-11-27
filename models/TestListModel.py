from pydantic import BaseModel


class TestListModel(BaseModel):
    test_list: list[int] | None = None
    total_count: int | None = None
