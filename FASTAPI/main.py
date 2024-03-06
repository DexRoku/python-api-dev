from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from models import Post, my_posts
from random import randrange

app = FastAPI()

#Refers to route/path operations.
#decorater helps us with the magic. we send get request method.
@app.get("/")
def root():
    return {"message": "welcome to my api"}

## For getting specific posts by id
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000000)    
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_posts():
    post = my_posts[len(my_posts)-1]
    return {"latest post": post}

# id field is called path parameter
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with {id} not found")
    #     response.status_code = status.HTTP_404_NOT_FOUND
    # return {"message": f"post with id : {id} was not found"}
## we want the user to send title str, content str.