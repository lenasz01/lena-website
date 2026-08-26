# How to Build a REST API

### How to setup backend with python fastapi
`pip install fastapi`

`pip install uvicorn`

use Git Bash terminal!

https://www.python.org/downloads/windows/ - download python

### How to start fastapi application with uvicorn
`uvicorn main:app --reload`

POST ITEMS > refresh server > GET item

### How to test fastapi application with uvicorn
POST curl: `curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"`

GET curl: `curl -X GET http://127.0.0.1:8000/items/0`

### Endpoints misc
GET - returns data

POST - sends info


### Error Handling
`import HTTPException`

`raise HTTPException(status_code=404, detail="Item not found")`

### list items
`curl -X GET http://127.0.0.1:8000/items?limit=3`

? denotes a parameter

### Models
```
class Item(BaseModel):
    text: str = None
    is_done: bool = False
```
Now, the Item is specified as a json `{"text": "apple","is_done": false}` instead of `"apple"`

This changes our curl command:

`curl -X POST -H "Content-Type: application/json" -d '{"text": "apple","is_done": false}' "http://127.0.0.1:8000/items"`

Add `response_model=Item` parameter to the tag @. Ex, `@app.get("/items/{item_id}", response_model=Item)`.

### Interactive documentation
`http://127.0.0.1:8000/docs#/` brings you to the swagger page

`http://127.0.0.1:8000/redoc` different ui