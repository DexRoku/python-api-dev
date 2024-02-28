from fastapi import FastAPI
from fastapi.params import Body
from models import Post, my_posts

app = FastAPI()

#Refers to route/path operations.
#decorater helps us with the magic. we send get request method.
@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}

## we want the user to send title str, content str.