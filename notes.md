# How to setup backend with python fastapi
`pip install fastapi`

`pip install uvicorn`

https://www.python.org/downloads/windows/ - download python

# How to start fastapi application with uvicorn
`uvicorn main:app --reload`

# How to test fastapi application with uvicorn
POST curl: `curl -X POST -H "Content-Type: application/json" "http://127.0.0.1:8000/items?item=apple"`

GET curl: `curl -X GET http://127.0.0.1:8000/items/0`

# Endpoints misc
GET - returns data
POST - sends info