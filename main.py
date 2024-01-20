from fastapi import FastAPI

from random import choice


app = FastAPI(title="LoveShop API")


@app.get("/main")
async def get_main():
    message = {"shop": "main page"}
    return message


categories = {
    "cat_1": "lubes",
    "cat_2": "dildos",
    "cat_3": "vibrators",
}


@app.get("/categories")
async def get_all_categories():
    return categories


@app.get("/categories/{category}")
async def get_category(category: str = "random"):
    if category == "random":
        random_category = choice(tuple(categories.values()))
        return {"your random item": random_category}

    if category in categories.keys():
        output = {"category": categories[category]}
        return output
    
    return {"error_message": "no such category"}


items = {
    1: "butt plug",
    2: "water based lube",
    3: "bodysuit",
}


@app.get("/items")
async def get_all_items():
    return items


@app.get("/items/{item_id}")
async def get_item(item_id: str = "random"):
    if item_id == "random":
        random_item = choice(tuple(items.values()))
        return {"your random item": random_item}
    
    if int(item_id) in items.keys():
        output = {"item": items[int(item_id)]}
        return output
    
    return {"error_message": "no such item"}
