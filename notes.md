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

### APIRouter
```
app = FastAPI
```
For creating the actual application. Runs, handles requests, and gets served by uvicorn. You can only have ONE of these per app.

```
router = APIRouter
```
Creates a collection of routes that isn't runnable on its own. Container you build up then PLUG INTO the main FastAPI() app.

# JWT Tokens

Once a user is authenticated, they are issued:
1. Refresh token
2. Access token - authorization (ensure user has credentials for the thing they're trying to access)

What does a JWT consist of?

`HEADER.PAYLOAD.SIGNATURE`

Take the Signature Produced by Server and check if it is equal to Signature in Token
If match => authorized
If not matched => not authorized

Anyone can alter JWT!! Never store information in JWTs

JWTs are stateless - JWT contains all the info in the tokens themselves, no DB lookups so server does not need to "remember" you. cannot be invalidated by the server

More items:
- JWT should be short lived 
- every time the token expires, the user will refresh the token

Mitigates the risk that someone will steal your token

## Fast API JWT
What you need to setup a route that requires a JWT token:
1. A way to use tokens - login endpoint that checks credentials and returns a signed JWT
2. A secret key - used to sign and verify tokens (keep this out of your code)
3. A library to create/verify JWTs
4. Middleware or decorator that checks incoming requestsfor a valid token before letting them hit the protected route

### How to setup JWT Tokens
auth.py verifies your tokens > routes folder files checks if token is verified > main.py wires everything together, making router objects actually readable

1. Create main.py, auth.py, routes folder with routes
2. auth.py should have all the "verifying tokens" functions. also create SECRET_KEY and put in .env
3. routers folder - create separate py files per each route. Set up your routes per endpoint
4. main.py remember to initialize all the routes
5. Create test token: `python -c "import jwt; print(jwt.encode({'sub': 'test'}, 'some-long-random-string-for-testing', algorithm='HS256'))"`
6. Open Swagger UI and put this in authorize

**Private Route**: protected behind JWT

**Public Route**: doesn't need authentication to see