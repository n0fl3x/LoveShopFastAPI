from pydantic import BaseModel


class PydCategories(BaseModel):
    name: str
    description: str | None = None


class PydTags(BaseModel):
    name: str


class PydItems(BaseModel):
    name: str
    price: float | int = 0.0
    description: str | None = None
    tags: list[PydTags] | None = None
