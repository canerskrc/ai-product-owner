from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class UserStory(BaseModel):
    id: int
    title: str
    description: str
    acceptance_criteria: List[str]
    priority: str
    story_points: int
    status: str
    created_at: datetime
    updated_at: datetime

class Sprint(BaseModel):
    id: int
    name: str
    start_date: datetime
    end_date: datetime
    goal: str
    status: str
    velocity: float
    created_at: datetime
    updated_at: datetime

class ProductBacklog(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    story_points: int
    sprint_id: Optional[int]
    created_at: datetime
    updated_at: datetime

class Stakeholder(BaseModel):
    id: int
    name: str
    role: str
    email: str
    created_at: datetime
    updated_at: datetime

class Feedback(BaseModel):
    id: int
    stakeholder_id: int
    content: str
    type: str
    priority: str
    status: str
    created_at: datetime
    updated_at: datetime 