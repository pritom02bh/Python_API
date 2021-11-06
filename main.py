from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True                # Optional Field
    rating: Optional[float] = None        # Return Null if no data send by users


 
@app.get("/")
def read_root():
    return {"message": "Welcome to my new API"}


@app.get("/posts")
def get_post():
    return {"data": "This is the post"}


@app.post("/createposts")
def create_post(post: Post):
    print(post)                 # Pydantic model  
    print(post.dict())          # Regular Python Dict.

    return {"data" : "post"}