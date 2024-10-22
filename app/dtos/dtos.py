from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    name: str
    email: str

class UserDTO(UserCreateDTO):
    id: int
    posts: Optional[List['PostDTO']] = []
    comments: Optional[List['CommentDTO']] = []

    class Config:
        orm_mode = True

class PostCreateDTO(BaseModel):
    title: str
    content: str
    status: PostStatus
    user_id: int

class PostDTO(PostCreateDTO):
    id: int
    user: Optional[UserDTO]
    tags: Optional[List['TagDTO']] = []
    comments: Optional[List['CommentDTO']] = []

    class Config:
        orm_mode = True

class CommentCreateDTO(BaseModel):
    content: str
    user_id: int
    post_id: int

class CommentDTO(CommentCreateDTO):
    id: int
    user: Optional[UserDTO]
    post: Optional[PostDTO]

    class Config:
        orm_mode = True

class TagCreateDTO(BaseModel):
    name: str

class TagDTO(TagCreateDTO):
    id: int
    posts: Optional[List[PostDTO]] = []

    class Config:
        orm_mode = True