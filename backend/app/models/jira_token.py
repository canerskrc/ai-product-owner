from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class JiraToken(Base):
    __tablename__ = "jira_tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    access_token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    cloud_id = Column(String, nullable=False)

    # opsiyonel: kullanıcıya geri erişim
    # user = relationship("User", back_populates="jira_token")
