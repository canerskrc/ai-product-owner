from pydantic import BaseModel
from uuid import UUID

class RequirementBase(BaseModel):
    title: str
    description: str

class RequirementCreate(RequirementBase):
    pass

class RequirementResponse(RequirementBase):
    id: UUID
    priority: int

    class Config:
        orm_mode = True

class FeedbackBase(BaseModel):
    requirement_id: UUID
    feedback_text: str

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackResponse(FeedbackBase):
    id: UUID

    class Config:
        orm_mode = True
