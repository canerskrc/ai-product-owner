from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from .entities import UserStory, Sprint, ProductBacklog, Stakeholder, Feedback

class UserStoryRepository(ABC):
    @abstractmethod
    async def create(self, user_story: UserStory) -> UserStory:
        pass

    @abstractmethod
    async def get_by_id(self, story_id: int) -> Optional[UserStory]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[UserStory]:
        pass

    @abstractmethod
    async def update(self, user_story: UserStory) -> UserStory:
        pass

    @abstractmethod
    async def delete(self, story_id: int) -> bool:
        pass

class SprintRepository(ABC):
    @abstractmethod
    async def create(self, sprint: Sprint) -> Sprint:
        pass

    @abstractmethod
    async def get_by_id(self, sprint_id: int) -> Optional[Sprint]:
        pass

    @abstractmethod
    async def get_active(self) -> Optional[Sprint]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Sprint]:
        pass

    @abstractmethod
    async def update(self, sprint: Sprint) -> Sprint:
        pass

    @abstractmethod
    async def delete(self, sprint_id: int) -> bool:
        pass

class ProductBacklogRepository(ABC):
    @abstractmethod
    async def create(self, backlog_item: ProductBacklog) -> ProductBacklog:
        pass

    @abstractmethod
    async def get_by_id(self, backlog_id: int) -> Optional[ProductBacklog]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[ProductBacklog]:
        pass

    @abstractmethod
    async def update(self, backlog_item: ProductBacklog) -> ProductBacklog:
        pass

    @abstractmethod
    async def delete(self, backlog_id: int) -> bool:
        pass

class StakeholderRepository(ABC):
    @abstractmethod
    async def create(self, stakeholder: Stakeholder) -> Stakeholder:
        pass

    @abstractmethod
    async def get_by_id(self, stakeholder_id: int) -> Optional[Stakeholder]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Stakeholder]:
        pass

    @abstractmethod
    async def update(self, stakeholder: Stakeholder) -> Stakeholder:
        pass

    @abstractmethod
    async def delete(self, stakeholder_id: int) -> bool:
        pass

class FeedbackRepository(ABC):
    @abstractmethod
    async def create(self, feedback: Feedback) -> Feedback:
        pass

    @abstractmethod
    async def get_by_id(self, feedback_id: int) -> Optional[Feedback]:
        pass

    @abstractmethod
    async def get_by_stakeholder(self, stakeholder_id: int) -> List[Feedback]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Feedback]:
        pass

    @abstractmethod
    async def update(self, feedback: Feedback) -> Feedback:
        pass

    @abstractmethod
    async def delete(self, feedback_id: int) -> bool:
        pass 