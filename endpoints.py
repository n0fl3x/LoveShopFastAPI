from random import choice
from typing import Annotated

from fastapi import Query

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
    

@app.get("/category/{category_name}")
async def get_category_by_name(
    category_name: str,
    add_str: Annotated[str | None, Query(max_length=16)] = None,
    ):
    cats_list = [cat.name for cat in EnumCategories]
    error_message = {"error message": "no such category"}

    if category_name in cats_list:
        if add_str:
            return {
                "category name": category_name,
                "category id": EnumCategories[f"{category_name}"].value,
                "added": EnumCategories[f"{category_name}"].name + " " + add_str,
            }
        else:
            return {
                "category name": category_name,
                "category id": EnumCategories[f"{category_name}"].value,
            }
        
    else:
        return error_message
    

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
    add_str: Annotated[str | None, Query(max_length=16)] = None,
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


@app.post("/tags/add")
async def add_new_tag(new_tag: PydTags):
    return new_tag


@app.delete("/categories/delete/{category}")
async def delete_category(category: str):
    cats_ids = [cat.value for cat in EnumCategories]
    cats_names = [cat.name for cat in EnumCategories]

    for n in cats_names:
        if n == category:
            return {
                "deleted_category_name": EnumCategories[f"{category}"].name,
                "deleted_category_id": EnumCategories[f"{category}"].value,
            }
    else:
        try:
            cat_id = int(category)
        except ValueError:
            return {"error_message": "no such category name or invalid category id"}
        
        for i in cats_ids:
                if i == cat_id:
                    return {
                        "deleted_category_name": EnumCategories(cat_id).name,
                        "deleted_category_id": EnumCategories(cat_id).value,
                    }


@app.delete("/items/delete/{item}")
async def delete_item(item: str):
    items_ids = [item.value for item in EnumItems]
    items_names = [item.name for item in EnumItems]

    for n in items_names:
        if n == item:
            return {
                "deleted_category_name": EnumItems[f"{item}"].name,
                "deleted_category_id": EnumItems[f"{item}"].value,
            }
    else:
        try:
            item_id = int(item)
        except ValueError:
            return {"error_message": "no such item name or invalid item id"}
        
        for i in items_ids:
                if i == item_id:
                    return {
                        "deleted_category_name": EnumItems(item_id).name,
                        "deleted_category_id": EnumItems(item_id).value,
                    }
