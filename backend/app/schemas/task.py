from pydantic import BaseModel
from typing import List

class FeatureRequest(BaseModel):
    feature_description: str

class TaskListResponse(BaseModel):
    tasks: List[str]

class JiraTaskCreateRequest(BaseModel):
    access_token: str
    project_key: str
    summary: str
    description: str
