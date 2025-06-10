from pydantic import BaseModel
from typing import List
from datetime import datetime
from typing import Optional

class FeatureRequest(BaseModel):
    feature_description: str

class TaskListResponse(BaseModel):
    tasks: List[str]

class JiraTaskCreateRequest(BaseModel):
    access_token: str
    project_key: str
    summary: str
    description: str

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "TODO"
    priority: str = "MEDIUM"
    sprint_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
