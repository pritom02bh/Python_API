from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()
class Post(BaseModel):
    title: str
    content: str
    published: bool = True                # Optional Field
    rating: Optional[float] = None        # Return Null if no data send by users


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
{"title": "Top laptop brands", "content": "Dell, Apple, HP, ASUS", "id": 2}]           # Saving the posts into memory

 
@app.get("/")
def read_root():
    return {"message": "Welcome to my new API"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)

    return {"data" : "post_dict"}