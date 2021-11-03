from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my new API"}


@app.get("/posts")
def get_post():
    return {"data": "This is the post"}

