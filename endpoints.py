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
async def get_category(category_id: Categories | RandomSomething):
    if category_id is RandomSomething.random:
        random_category = choice(tuple(Categories))
        return {"your random category": random_category.name}

    categories_vals = [cat.value for cat in Categories]
    if Categories(category_id).value in categories_vals:
        output = {"category": Categories(category_id).name}
        return output
    
    return {"error_message": "no such category"}


@app.get("/items")
async def get_all_items():
    return {"all items": [item.name for item in Items]}


@app.get("/items/{item_id}")
async def get_item(item_id: Items | RandomSomething):
    if item_id is RandomSomething.random:
        random_item = choice(tuple(Items))
        return {"your random item": random_item.name}
    
    items_vals = [item.value for item in Items]
    if Items(item_id).value in items_vals:
        output = {"item": Items(item_id).name}
        return output
    
    return {"error_message": "no such item"}
