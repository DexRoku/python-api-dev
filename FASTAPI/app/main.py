from fastapi import FastAPI, Response, status, HTTPException
from models import Post, my_posts
from random import randrange

app = FastAPI()

# Define functions to find posts and their indexes
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

# Define root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to my API"}

# Define endpoint to get all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# Define endpoint to create a new post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# Define endpoint to get the latest post
@app.get("/posts/latest")
def get_latest_post():
    if len(my_posts) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    latest_post = my_posts[-1]
    return {"latest_post": latest_post}

# Define endpoint to get a specific post by id
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return {"data": post}

# Define endpoint to delete a post by id
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Define endpoint to update a post by id
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    my_posts[index] = post.dict()
    my_posts[index]['id'] = id
    return {"message": f"Post with id {id} updated successfully"}