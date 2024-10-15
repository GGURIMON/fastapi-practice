from fastapi import APIRouter, status, Request
from pydantic import BaseModel
router = APIRouter(
    prefix = "/blog",
    tags= ["blog"]
)

class BlogModel(BaseModel):
    userText: str
    content: str
    imageMap: list

@router.post('/new')
def create_blog(blog: BaseModel):
    return "Ok"