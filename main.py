from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my new API"}


@app.get("/posts")
def get_post():
    return {"data": "This is the post"}

