from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str

 
@app.get("/")
def read_root():
    return {"message": "Welcome to my new API"}


@app.get("/posts")
def get_post():
    return {"data": "This is the post"}


@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post.title)
    print(new_post.content)
    return {"data" : "new_post"}