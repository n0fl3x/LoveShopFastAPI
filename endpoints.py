from random import choice

from application import app
from models import Categories, Items


@app.get("/main")
async def get_main():
    message = {"shop": "main page"}
    return message


@app.get("/categories")
async def get_all_categories():
    return {"all categories": [cat_name.value for cat_name in Categories]}


@app.get("/categories/{category_id}")
async def get_category(category_id: str = "random"):
    if category_id == "random":
        random_category = choice(tuple(Categories))
        return {"your random category": random_category}

    categories_id = [cat.name for cat in Categories]
    if category_id in categories_id:
        output = {"category": Categories[category_id].value}
        return output
    
    return {"error_message": "no such category"}


@app.get("/items")
async def get_all_items():
    return {"all items": [item_name.value for item_name in Items]}


@app.get("/items/{item_id}")
async def get_item(item_id: str = "random"):
    if item_id == "random":
        random_item = choice(tuple(Items))
        return {"your random item": random_item}
    
    items_id = [item.name for item in Items]
    if item_id in items_id:
        output = {"item": Items[item_id].value}
        return output
    
    return {"error_message": "no such item"}
