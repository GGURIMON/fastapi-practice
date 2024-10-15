from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/blog/me")
def get_blog_me():
    return {"message": "my blog"}

@app.get('/blog/q')
def get_blog_search(page, page_size: Optional[int] = None):
    return {"message": f"you can get your blog on {page} and your page size is {page_size}"}

@app.get('/blog/{id}/comments/{comment_id}')
def user_get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"my message": f"blog_id: {id}, comment id: {comment_id}, valid: {valid}, username: {username}"}

@app.get('/blog/{id}')
def get_blog(id):
    return {"message": f"blog with {id}"}

# Enum 정의 수정 (콜론 대신 = 사용)
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f"Blog type: {type}"}


