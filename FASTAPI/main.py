from fastapi import FastAPI
from fastapi.params import Body
from models import Post, my_posts
from random import randrange


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
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000000)    
    my_posts.append(post_dict)
    return {"data": post_dict}

## we want the user to send title str, content str.