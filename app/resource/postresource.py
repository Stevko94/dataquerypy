from fastapi.routing import APIRouter
from typing import List, Optional

post_router = APIRouter()
user_router = APIRouter()

@post_router.get("/posts/", response_model=List[PostDTO])
def get_posts(status: Optional[PostStatus] = Query(None), include: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Post)
    if status:
        query = query.filter(Post.status == status)
    query = get_includes(query, include, Post)
    return query.all()

@post_router.get("/posts/{post_id}", response_model=PostDTO)
def get_post(post_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Post).filter(Post.id == post_id)
    query = get_includes(query, include, Post)
    post = query.first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# User endpoints
@user_router.get("/users/{user_id}", response_model=UserDTO)
def get_user(user_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(User).filter(User.id == user_id)
    query = get_includes(query, include, User)
    user = query.first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
