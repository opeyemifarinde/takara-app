from fastapi import APIRouter

from . import users, stories

# Central API router for including all sub-routers
api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(stories.router, prefix="/stories", tags=["stories"])
