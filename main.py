import fastapi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str
    is_done: bool = False


items = []

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item created", "item": item}

@app.get("/items", response_model=list[Item])
def list_items(skip: int = 0, limit: int = 10):
    if skip < 0 or limit <= 0:
        raise HTTPException(status_code=400, detail="Invalid skip or limit")
    return items[skip: skip + limit]


# get by item id
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    # return {"item": items[item_id]}
    return items[item_id]

