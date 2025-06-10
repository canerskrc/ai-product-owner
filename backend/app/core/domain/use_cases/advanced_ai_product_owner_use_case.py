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
from app.core.services.advanced_ai_service import AdvancedAIProductOwner

class AdvancedAIProductOwnerUseCase:
    """Gelişmiş AI Product Owner use case implementation"""

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
        self.ai_agent = AdvancedAIProductOwner()

    async def create_and_analyze_user_story(self, story_data: Dict[str, Any]) -> Dict[str, Any]:
        """User story oluşturur ve gelişmiş AI analizi yapar."""
        # Gelişmiş AI analizi
        analysis = await self.ai_agent.analyze_user_story(
            story=story_data["description"],
            context={
                "project_context": story_data.get("project_context"),
                "team_capacity": story_data.get("team_capacity"),
                "technical_constraints": story_data.get("technical_constraints"),
                "business_goals": story_data.get("business_goals"),
                "market_conditions": story_data.get("market_conditions")
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
            updated_at=datetime.utcnow(),
            complexity=analysis["complexity_analysis"]["total_complexity"],
            business_value=analysis["value_analysis"].get("total_value", 0),
            risk_level=analysis["risk_analysis"].get("risk_level", "MEDIUM")
        )

        # Veritabanına kaydetme
        created_story = await self.user_story_repo.create(story)

        return {
            "story": created_story,
            "analysis": analysis
        }

    async def prioritize_and_plan_sprint(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint planlaması yapar ve backlog'u gelişmiş önceliklendirme ile değerlendirir."""
        # Backlog önceliklendirme
        backlog_items = await self.backlog_repo.get_all()
        prioritization = await self.ai_agent.prioritize_backlog(
            items=[item.dict() for item in backlog_items],
            context={
                "team_capacity": sprint_data.get("team_capacity"),
                "sprint_goals": sprint_data.get("goals"),
                "technical_constraints": sprint_data.get("constraints"),
                "business_priorities": sprint_data.get("business_priorities"),
                "resource_availability": sprint_data.get("resource_availability")
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
            updated_at=datetime.utcnow(),
            team_capacity=sprint_data.get("team_capacity"),
            business_priority=sprint_data.get("business_priority", "MEDIUM")
        )

        # Veritabanına kaydetme
        created_sprint = await self.sprint_repo.create(sprint)

        return {
            "sprint": created_sprint,
            "prioritization": prioritization
        }

    async def analyze_sprint_performance(self, sprint_id: int) -> Dict[str, Any]:
        """Sprint performansını gelişmiş analiz teknikleri ile değerlendirir."""
        # Sprint verilerini alma
        sprint = await self.sprint_repo.get_by_id(sprint_id)
        if not sprint:
            raise ValueError("Sprint not found")

        # Sprint performans analizi
        performance = await self.ai_agent.analyze_sprint_performance({
            "sprint": sprint.dict(),
            "stories": [story.dict() for story in await self.user_story_repo.get_all()],
            "velocity": sprint.velocity,
            "team_metrics": sprint.team_metrics if hasattr(sprint, "team_metrics") else {},
            "quality_metrics": sprint.quality_metrics if hasattr(sprint, "quality_metrics") else {}
        })

        # Gelecek performans tahmini
        future_performance = await self.ai_agent.predict_future_performance({
            "historical_data": {
                "sprints": [s.dict() for s in await self.sprint_repo.get_all()],
                "stories": [s.dict() for s in await self.user_story_repo.get_all()],
                "team_metrics": performance["team_performance"]["metrics"]
            }
        })

        return {
            "current_performance": performance,
            "future_predictions": future_performance
        }

    async def generate_comprehensive_report(self, sprint_id: int) -> Dict[str, Any]:
        """Kapsamlı sprint raporu oluşturur."""
        # Sprint verilerini alma
        sprint = await self.sprint_repo.get_by_id(sprint_id)
        if not sprint:
            raise ValueError("Sprint not found")

        # Sprint performans analizi
        performance = await self.analyze_sprint_performance(sprint_id)

        # Stakeholder geri bildirimleri
        feedbacks = await self.feedback_repo.get_all()
        stakeholders = await self.stakeholder_repo.get_all()

        return {
            "sprint_summary": sprint.dict(),
            "performance_analysis": performance,
            "stakeholder_feedback": {
                "feedbacks": [f.dict() for f in feedbacks],
                "stakeholders": [s.dict() for s in stakeholders]
            },
            "recommendations": performance["current_performance"]["recommendations"],
            "future_outlook": performance["future_predictions"]
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