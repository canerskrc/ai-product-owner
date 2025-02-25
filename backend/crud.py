from sqlalchemy.orm import Session
from models import Requirement, Feedback
from schemas import RequirementCreate, FeedbackCreate
import uuid

def get_requirements(db: Session):
    return db.query(Requirement).all()

def create_requirement(db: Session, requirement: RequirementCreate):
    new_requirement = Requirement(
        id=uuid.uuid4(),
        title=requirement.title,
        description=requirement.description
    )
    db.add(new_requirement)
    db.commit()
    db.refresh(new_requirement)
    return new_requirement
