from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/")
def index():
    return {"message":"Hello World"}

@app.get("/blog/me", tags=['blog'])
def get_blog_me():
    return {"message": "my blog"}

@app.get('/blog/q', tags=['blog', 'query'])
def get_blog_search(page, page_size: Optional[int] = None):
    return {"message": f"you can get your blog on {page} and your page size is {page_size}"}

@app.get('/blog/{id}/comments/{comment_id}',tags=['blog'])
def user_get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"my message": f"blog_id: {id}, comment id: {comment_id}, valid: {valid}, username: {username}"}

@app.get('/blog/{id}', tags=['blog'])
def get_blog(id):
    return {"message": f"blog with {id}"}

# Enum 정의 수정 (콜론 대신 = 사용)
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {"message": f"Blog type: {type}"}

@app.get('/naver/search/{query}', status_code = status.HTTP_200_OK, tags=['query'], summary= "status code testing", description= "status code with temp situation for learning")
def get_search_naver(query: int, response: Response):
    if query > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"{query} page not found!"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"here is your {query} page!"}