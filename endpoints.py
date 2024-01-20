from random import choice

from application import app
from models import (
    RandomSomething,
    Categories,
    Items,
)


@app.get("/main")
async def get_main():
    message = {"shop": "main page"}
    return message


@app.get("/categories")
async def get_all_categories():
    return {"all categories": [cat.name for cat in Categories]}


@app.get("/categories/{category_id}")
async def get_category(
    category_id: Categories | RandomSomething,
    end: int | None = None,
    desc: bool | None = None,
    ):
    if not end:
        if category_id is RandomSomething.random:
            random_category = choice(tuple(Categories))
            return {"your random category": random_category.name}

        categories_vals = [cat.value for cat in Categories]
        if Categories(category_id).value in categories_vals:
            output = {"category": Categories(category_id).name}
            return output
    
        return {"error_message": "no such category"}
    else:
        cats_list = [cat.name for cat in Categories]

        if len(Categories) >= end:
            limited_list = cats_list[(category_id - 1):end]
        else:
            limited_list = cats_list[(category_id - 1):len(Categories)]

        return limited_list if not desc else limited_list[::-1]


@app.get("/items")
async def get_all_items():
    return {"all items": [item.name for item in Items]}


@app.get("/items/{item_id}")
async def get_item(
    item_id: Items | RandomSomething,
    end: int | None = None,
    desc: bool | None = None,
    ):
    if not end:
        if item_id is RandomSomething.random:
            random_item = choice(tuple(Items))
            return {"your random item": random_item.name}
    
        items_vals = [item.value for item in Items]
        if Items(item_id).value in items_vals:
            output = {"item": Items(item_id).name}
            return output
    
        return {"error_message": "no such item"}
    else:
        items_list = [item.name for item in Items]

        if len(Items) >= end:
            limited_list = items_list[(item_id - 1):end]
        else:
            limited_list = items_list[(item_id - 1):len(Items)]
        
        return limited_list if not desc else limited_list[::-1]
    