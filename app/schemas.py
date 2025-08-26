from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# User schemas
class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str


class User(UserBase):
    id: str
    role: str
    created_at: datetime

    class Config:
        orm_mode = True


# Story schemas
class StoryBase(BaseModel):
    title: str
    content: str
    genre: str
    language: str
    region: Optional[str] = None
    cover_image_url: Optional[str] = None
    is_draft: Optional[bool] = False


class StoryCreate(StoryBase):
    """Schema for creating a story."""
    pass


class Story(StoryBase):
    id: str
    author_id: str
    read_count: int
    bookmark_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Bookmark schema
class Bookmark(BaseModel):
    id: str
    user_id: str
    story_id: str
    created_at: datetime

    class Config:
        orm_mode = True


# Follow schema
class Follow(BaseModel):
    id: str
    follower_id: str
    following_id: str
    created_at: datetime

    class Config:
        orm_mode = True
