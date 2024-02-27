from fastapi import FastAPI
from fastapi.params import Body
from models import Post

app = FastAPI()




#Refers to route/path operations.
#decorater helps us with the magic. we send get request method.
@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": " This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post}

## we want the user to send title str, content str.