from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Story)
def create_story(story: schemas.StoryCreate, db: Session = Depends(get_db)):
    # Ensure the author exists
    author = db.query(models.User).filter(models.User.id == story.author_id).first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    new_story = models.Story(**story.dict())
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return new_story

@router.get("/", response_model=List[schemas.Story])
def read_stories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stories = db.query(models.Story).filter(models.Story.is_draft == False).offset(skip).limit(limit).all()
    return stories
