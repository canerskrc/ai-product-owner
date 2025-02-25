from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Feedback, Requirement
from schemas import FeedbackCreate, FeedbackResponse
import uuid

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/", response_model=FeedbackResponse)
def add_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
 
    requirement = db.query(Requirement).filter(Requirement.id == feedback.requirement_id).first()
    if not requirement:
        raise HTTPException(status_code=404, detail="Requirement not found")

    new_feedback = Feedback(
        id=uuid.uuid4(),
        requirement_id=feedback.requirement_id,
        feedback_text=feedback.feedback_text
    )
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback

@router.get("/{requirement_id}", response_model=list[FeedbackResponse])
def get_feedback(requirement_id: uuid.UUID, db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).filter(Feedback.requirement_id == requirement_id).all()
    if not feedbacks:
        raise HTTPException(status_code=404, detail="No feedback found for this requirement")
    return feedbacks
