from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from .entities import UserStory, Sprint, ProductBacklog, Stakeholder, Feedback
from .repositories import (
    UserStoryRepository,
    SprintRepository,
    ProductBacklogRepository,
    StakeholderRepository,
    FeedbackRepository
)

class ProductOwnerUseCase(ABC):
    def __init__(
        self,
        user_story_repo: UserStoryRepository,
        sprint_repo: SprintRepository,
        backlog_repo: ProductBacklogRepository,
        stakeholder_repo: StakeholderRepository,
        feedback_repo: FeedbackRepository
    ):
        self.user_story_repo = user_story_repo
        self.sprint_repo = sprint_repo
        self.backlog_repo = backlog_repo
        self.stakeholder_repo = stakeholder_repo
        self.feedback_repo = feedback_repo

    @abstractmethod
    async def create_user_story(self, story: UserStory) -> UserStory:
        pass

    @abstractmethod
    async def prioritize_backlog(self) -> List[ProductBacklog]:
        pass

    @abstractmethod
    async def plan_sprint(self, sprint: Sprint) -> Sprint:
        pass

    @abstractmethod
    async def analyze_feedback(self) -> dict:
        pass

    @abstractmethod
    async def generate_sprint_report(self, sprint_id: int) -> dict:
        pass

class AIProductOwnerUseCase(ProductOwnerUseCase):
    async def create_user_story(self, story: UserStory) -> UserStory:
        # AI ile user story analizi ve iyileştirme
        return await self.user_story_repo.create(story)

    async def prioritize_backlog(self) -> List[ProductBacklog]:
        # AI ile backlog önceliklendirme
        backlog_items = await self.backlog_repo.get_all()
        # AI analizi ve önceliklendirme mantığı
        return backlog_items

    async def plan_sprint(self, sprint: Sprint) -> Sprint:
        # AI ile sprint planlaması
        return await self.sprint_repo.create(sprint)

    async def analyze_feedback(self) -> dict:
        # AI ile geri bildirim analizi
        feedbacks = await self.feedback_repo.get_all()
        # AI analizi ve öneriler
        return {
            "analysis": "AI analysis results",
            "recommendations": ["Recommendation 1", "Recommendation 2"]
        }

    async def generate_sprint_report(self, sprint_id: int) -> dict:
        # AI ile sprint raporu oluşturma
        sprint = await self.sprint_repo.get_by_id(sprint_id)
        if not sprint:
            raise ValueError("Sprint not found")
        
        return {
            "sprint_info": sprint,
            "velocity": sprint.velocity,
            "recommendations": ["AI recommendation 1", "AI recommendation 2"]
        } 