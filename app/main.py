from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI(root_path="/app")

class NameRequest(BaseModel):
    name: str

@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Xin chào {name}"}

@app.post("/hello")
def say_hello_post(request: NameRequest):
    return {"message": f"Xin chào {request.name} test1"}
