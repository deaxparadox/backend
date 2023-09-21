from enum import Enum
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult


from app.service.logging import logging
from app.celery.tasks import (
    create_task,
    fibonacci
)


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]


logging.debug("App instance")
app = FastAPI()


################################ 
#           CELERY             #
################################

@app.get("/celery")
async def celery_worker():
    task = create_task.delay(int(1))
    return {
        "task_id": task.id
    }




@app.get("/celery/fibonacci/{number}")
async def celery_worker(
    number: int
):
    task = fibonacci.delay(number)
    return {
        "task_id": task.id
    }

@app.get("/celery/result")
async def celery_worker(
    task_id: str
):
    task_result = AsyncResult(task_id)
    result = {}
    if task_result.ready():
        result.update({
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": task_result.result,
            "task_valud": task_result.get()
        })
    else:
        result.update({
            "task_id": task_id,
            "task_status": None,
            "task_result": None
        })
    return JSONResponse(result)



################################ 
#           FastAPI            #
################################

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
async def read_item(
        item_id: int,
        q: str | None = None,
        skip: int = 0, 
        limit: int = 10,
        short: bool = False
    ):
    logging.debug(f"{read_item.__name__}:/items/{item_id}:path and query parameter")
    item = {
        "item_id": item_id, 
        "fake_items_db": fake_items_db[skip : skip + limit]
    }

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: int,
    q: str | None = None,
    skip: int = 0, 
    limit: int = 10,
    short: bool = False
):
    logging.debug(f"{read_item.__name__}:/items/{item_id}:path and query parameter")
    item = {
        "item_id": item_id, 
        "owner_id": user_id, 
        "fake_items_db": fake_items_db[skip : skip + limit]
    }

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item