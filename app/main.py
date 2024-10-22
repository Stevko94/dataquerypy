from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import sessionmaker, Session, relationship
from typing import List, Optional

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_includes(query, include: Optional[str], model):
    if include:
        relationships = include.split(',')
        for relation in relationships:
            if hasattr(model, relation):
                query = query.options(relationship(relation))
    return query

app = FastAPI()

# Include the routers
app.include_router(post_router, prefix="/api")
app.include_router(user_router, prefix="/api")


