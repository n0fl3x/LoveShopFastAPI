from random import choice
from fastapi import Query
from typing import Annotated
from application import app
from pydantic_classes import(
    PydCategories,
    PydItems,
    PydTags,
)

from enum_classes import (
    EnumRandomSomething,
    EnumCategories,
    EnumItems,
)


@app.get("/main")
async def get_main():
    all_categories = [cat.name for cat in EnumCategories]
    all_items = [item.name for item in EnumItems]
    result = {
        "all categories": all_categories,
        "all items": all_items,
    }
    
    return result


@app.get("/categories")
async def get_all_categories():
    return {"all categories": [cat.name for cat in EnumCategories]}


@app.get("/categories/{category_id}")
async def get_category_by_id(
    category_id: EnumCategories | EnumRandomSomething,
    end: int | None = None,
    desc: bool | None = None,
    ):
    if not end:
        if category_id is EnumRandomSomething.random:
            random_category = choice(tuple(EnumCategories))
            return {"your random category": random_category.name}

        categories_vals = [cat.value for cat in EnumCategories]
        if EnumCategories(category_id).value in categories_vals:
            output = {"category": EnumCategories(category_id).name}
            return output
    
        return {"error_message": "no such category"}
    else:
        cats_list = [cat.name for cat in EnumCategories]

        if len(EnumCategories) >= end:
            limited_list = cats_list[(category_id - 1):end]
        else:
            limited_list = cats_list[(category_id - 1):len(EnumCategories)]

        return limited_list if not desc else limited_list[::-1]
    

@app.get("/items")
async def get_all_items():
    return {"all items": [item.name for item in EnumItems]}


@app.get("/items/{item_id}")
async def get_item_by_id(
    item_id: EnumItems | EnumRandomSomething,
    end: int | None = None,
    desc: bool | None = None,
    ):
    if not end:
        if item_id is EnumRandomSomething.random:
            random_item = choice(tuple(EnumItems))
            return {"your random item": random_item.name}
    
        items_vals = [item.value for item in EnumItems]
        if EnumItems(item_id).value in items_vals:
            output = {"item": EnumItems(item_id).name}
            return output
    
        return {"error_message": "no such item"}
    else:
        items_list = [item.name for item in EnumItems]

        if len(EnumItems) >= end:
            limited_list = items_list[(item_id - 1):end]
        else:
            limited_list = items_list[(item_id - 1):len(EnumItems)]
        
        return limited_list if not desc else limited_list[::-1]
    

@app.get("/item/{item_name}")
async def get_item_by_name(
    item_name: str,
    add_str: Annotated[str | None, Query(max_length=7, min_length=3)] = None,
    ):
    items_list = [item.name for item in EnumItems]
    error_message = {"error message": "no such item"}

    if item_name in items_list:
        if add_str:
            return {
                "item name": item_name,
                "item id": EnumItems[f"{item_name}"].value,
                "added": EnumItems[f"{item_name}"].name + " " + add_str,
            }
        else:
            return {
                "item name": item_name,
                "item id": EnumItems[f"{item_name}"].value,
            }
        
    else:
        return error_message


@app.post("/categories/add")
async def add_new_category(new_category: PydCategories):
    return new_category


@app.post("/items/add")
async def add_new_item(new_item: PydItems):
    return new_item
