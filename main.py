from fastapi import FastAPI
from fastaapi.middleware.cors import CORSMiddleware



app = FastAPI(title="TÀKÀRÀ API", version="0.1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to TÀKÀRÀ API"}

# TODO: Add routers for users, s

from app.database import Base, engine
from app.routers import api_router

Base.metadata.create_all(bind=engine)
app.include_router(api_router)
