from service.logging import logging

from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


logging.debug("App instance")
app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    logging.debug(f"{get_model.__name__}:/models/{model_name}:return requested model")
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/")
async def root():
    logging.debug(f"call to root...")
    return {
        "message": "Hello world"
    }

@app.get("/users/me")
async def read_user_me():
    logging.debug(f"{read_user_me.__name__}:/users/me:get the current user")
    return {
        "user_id": "the current user"
    }

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    logging.debug(f"{read_user.__name__}:/users/{user_id}:accept and return current user_id")
    return {
        "user_id": user_id
    }

@app.get("/users")
async def read_users():
    logging.debug(f"{read_users.__name__}:/users:get all user")
    return [
        "Rick", 
        "Morty"
    ]

@app.get("/users")
async def read_users2():
    return [
        "Bean",
        "Elfo"
    ]

@app.get("/items/{item_id}")
async def read_item(item_id: int, skip: int = 0, limit: int = 10):
    logging.debug(f"{read_item.__name__}:/items/{item_id}:path and query parameter")
    return {
        "item_id": item_id, 
        "fake_items_db": fake_items_db[skip : skip + limit]
    }