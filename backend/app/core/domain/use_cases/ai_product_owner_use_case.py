from typing import List, Dict, Any, Optional
from datetime import datetime
from app.core.domain.entities import UserStory, Sprint, ProductBacklog, Stakeholder, Feedback
from app.core.domain.repositories import (
    UserStoryRepository,
    SprintRepository,
    ProductBacklogRepository,
    StakeholderRepository,
    FeedbackRepository
)
from app.core.services.ai_service import AIProductOwnerAgent

class AIProductOwnerUseCase:
    """AI Product Owner use case implementation"""

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
        self.ai_agent = AIProductOwnerAgent()

    async def create_and_analyze_user_story(self, story_data: Dict[str, Any]) -> Dict[str, Any]:
        """User story oluşturur ve AI ile analiz eder."""
        # AI analizi
        analysis = await self.ai_agent.analyze_user_story(
            story=story_data["description"],
            context={
                "project_context": story_data.get("project_context"),
                "team_capacity": story_data.get("team_capacity"),
                "technical_constraints": story_data.get("technical_constraints")
            }
        )

        # User story oluşturma
        story = UserStory(
            title=story_data["title"],
            description=story_data["description"],
            acceptance_criteria=analysis.get("recommendations", []),
            priority=story_data.get("priority", "MEDIUM"),
            story_points=analysis["story_points"],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        # Veritabanına kaydetme
        created_story = await self.user_story_repo.create(story)

        return {
            "story": created_story,
            "analysis": analysis
        }

    async def prioritize_and_plan_sprint(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint planlaması yapar ve backlog'u önceliklendirir."""
        # Backlog önceliklendirme
        backlog_items = await self.backlog_repo.get_all()
        prioritization = await self.ai_agent.prioritize_backlog(
            items=[item.dict() for item in backlog_items],
            context={
                "team_capacity": sprint_data.get("team_capacity"),
                "sprint_goals": sprint_data.get("goals"),
                "technical_constraints": sprint_data.get("constraints")
            }
        )

        # Sprint oluşturma
        sprint = Sprint(
            name=sprint_data["name"],
            start_date=sprint_data["start_date"],
            end_date=sprint_data["end_date"],
            goal=sprint_data["goal"],
            status="PLANNING",
            velocity=0.0,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        # Veritabanına kaydetme
        created_sprint = await self.sprint_repo.create(sprint)

        return {
            "sprint": created_sprint,
            "prioritization": prioritization
        }

    async def analyze_sprint_performance(self, sprint_id: int) -> Dict[str, Any]:
        """Sprint performansını analiz eder."""
        # Sprint verilerini alma
        sprint = await self.sprint_repo.get_by_id(sprint_id)
        if not sprint:
            raise ValueError("Sprint not found")

        # Sprint performans analizi
        performance = await self.ai_agent.analyze_sprint_performance({
            "sprint": sprint.dict(),
            "stories": [story.dict() for story in await self.user_story_repo.get_all()],
            "velocity": sprint.velocity
        })

        return performance

    async def generate_comprehensive_report(self, sprint_id: int) -> Dict[str, Any]:
        """Kapsamlı sprint raporu oluşturur."""
        # Sprint verilerini alma
        sprint = await self.sprint_repo.get_by_id(sprint_id)
        if not sprint:
            raise ValueError("Sprint not found")

        # Sprint raporu oluşturma
        report = await self.ai_agent.generate_sprint_report({
            "sprint": sprint.dict(),
            "stories": [story.dict() for story in await self.user_story_repo.get_all()],
            "performance": await self.analyze_sprint_performance(sprint_id)
        })

        return report

    async def analyze_stakeholder_feedback(self) -> Dict[str, Any]:
        """Stakeholder geri bildirimlerini analiz eder."""
        # Geri bildirimleri alma
        feedbacks = await self.feedback_repo.get_all()
        stakeholders = await self.stakeholder_repo.get_all()

        # Geri bildirim analizi
        analysis = await self.ai_agent.analyze_stakeholder_feedback(feedbacks)

        return {
            "analysis": analysis,
            "stakeholders": stakeholders
        }

    async def update_story_status(self, story_id: int, new_status: str) -> UserStory:
        """User story durumunu günceller ve ilgili analizleri yapar."""
        # Story'yi alma
        story = await self.user_story_repo.get_by_id(story_id)
        if not story:
            raise ValueError("Story not found")

        # Durum güncelleme
        story.status = new_status
        story.updated_at = datetime.utcnow()

        # Veritabanını güncelleme
        updated_story = await self.user_story_repo.update(story)

        # Eğer story tamamlandıysa, sprint analizini güncelle
        if new_status == "DONE":
            sprint = await self.sprint_repo.get_by_id(story.sprint_id)
            if sprint:
                await self.analyze_sprint_performance(sprint.id)

        return updated_story 