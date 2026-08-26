from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# This is a Model object
class Item(BaseModel):
    text: str
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"Hello" : "World!"}

# uvicorn main:app --reload

# when item was str: curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"
# when item is a Model object: curl -X POST -H "Content-Type: application/json" -d '{"text": "apple","is_done": false}' "http://127.0.0.1:8000/items"
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

# curl -X GET http://127.0.0.1:8000/items?limit=3
@app.get("/items", response_model=list[Item])
def get_item(limit: int = 10):
    return items[0:limit]

# curl -X GET http://127.0.0.1:8000/items/0
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")