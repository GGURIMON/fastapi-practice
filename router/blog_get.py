from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix = "/blog",
    tags = ["blog"]
)

@router.get("/me")
def get_blog_me():
    return {"message": "my blog"}

@router.get('/q', tags= ['query'])
def get_blog_search(page, page_size: Optional[int] = None):
    return {"message": f"you can get your blog on {page} and your page size is {page_size}"}

@router.get('/{id}/comments/{comment_id}')
def user_get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"my message": f"blog_id: {id}, comment id: {comment_id}, valid: {valid}, username: {username}"}

@router.get('/{id}')
def get_blog(id):
    return {"message": f"blog with {id}"}

# Enum 정의 수정 (콜론 대신 = 사용)
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    """
    this is more easier to explain for me and easier to write
    ### BlogType
    * short
    * story
    * howto
    """

    return {"message": f"Blog type: {type}"}

@router.get('/search/{query}', 
    status_code = status.HTTP_200_OK,
    tags=['query'], 
    summary= "status code testing", 
    description= "status code with temp situation for learning",
    response_description= "this is a response description"
    )
def get_search_naver(query: int, response: Response):
    if query > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"{query} page not found!"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"here is your {query} page!"}