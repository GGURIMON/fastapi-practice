from fastapi import APIRouter, Query
from pydantic import BaseModel
router = APIRouter(
    prefix = "/blog",
    tags= ["blog"]
)

class BlogModel(BaseModel):
    userText: str
    content: str
    imageMap: list

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
    }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, comment_id: int = Query(None, title="id of the comment", description="Some description for comment_id", alias="commentId", deprecated=True) ):
    pass