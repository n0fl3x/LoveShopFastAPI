from pydantic import BaseModel, Field


class PydCategories(BaseModel):
    cat_name: str = Field(min_length=3, max_length=32)
    cat_description: str | None = None


class PydTags(BaseModel):
    tag_name: str = Field(min_length=2, max_length=16)


class PydItems(BaseModel):
    item_name: str = Field(min_length=2, max_length=128)
    item_price: float | int = Field(ge=0.0)
    item_description: str | None = None
    item_tags: list[PydTags] = None
