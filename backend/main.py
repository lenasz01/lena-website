from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"Hello" : "World!"}

# uvicorn main:app --reload
# how to post: curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"
@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item
