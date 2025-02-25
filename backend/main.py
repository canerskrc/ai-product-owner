from fastapi import FastAPI
from database import engine
from models import Base
from routers import auth, requirements, feedback, users
import redis

# FastAPI 
app = FastAPI()

Base.metadata.create_all(bind=engine)

# Redis
redis_client = redis.Redis(host="redis", port=6379, db=0)

# Router'ları ekleyelim
app.include_router(auth.router)
app.include_router(requirements.router)
app.include_router(feedback.router)
app.include_router(users.router)

@app.get("/")
def health_check():
    return {"status": "API is running"}
