from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = [{"title": "title of post 1", "content": "content of post1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]
