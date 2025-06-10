from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logger import init_logging
from app.database.session import engine
from app.database.base import Base
from app.routers import auth, users, requirements, feedback, jira, reports, tasks
from redis.asyncio import Redis

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Initialize logging
init_logging()

# Initialize DB models
Base.metadata.create_all(bind=engine)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(requirements.router, prefix="/requirements", tags=["Requirements"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(jira.router, prefix="/jira", tags=["Jira"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(tasks.router, prefix=f"{settings.API_V1_STR}/tasks", tags=["tasks"])

@app.on_event("startup")
async def startup_event():
    app.state.redis = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0,
        decode_responses=True
    )
    await app.state.redis.ping()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Product Owner API"}