from typing import List, Dict, Any, Optional
from datetime import datetime
import torch
import numpy as np
from app.core.domain.entities import UserStory, Sprint, ProductBacklog, Stakeholder, Feedback
from app.core.domain.repositories import (
    UserStoryRepository,
    SprintRepository,
    ProductBacklogRepository,
    StakeholderRepository,
    FeedbackRepository
)
from app.core.services.deep_learning_ai_service import DeepLearningAIProductOwner

class DeepLearningAIProductOwnerUseCase:
    """Derin öğrenme yetenekleri ile donatılmış AI Product Owner use case implementation"""

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
        self.ai_agent = DeepLearningAIProductOwner()

    async def create_and_analyze_user_story(self, story_data: Dict[str, Any]) -> Dict[str, Any]:
        """User story oluşturur ve derin öğrenme ile analiz eder."""
        # Derin öğrenme analizi
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
            acceptance_criteria=analysis.get("agent_recommendation", {}).get("recommendations", []),
            priority=story_data.get("priority", "MEDIUM"),
            story_points=analysis["story_points"],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            complexity=analysis["complexity_analysis"]["technical_complexity"],
            business_value=analysis["complexity_analysis"]["business_complexity"],
            risk_level=analysis["risk_assessment"]["technical_risk"]
        )

        # Veritabanına kaydetme
        created_story = await self.user_story_repo.create(story)

        # Model eğitimi için veri toplama
        self._collect_training_data(story, analysis)

        return {
            "story": created_story,
            "analysis": analysis
        }

    async def prioritize_and_plan_sprint(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint planlaması yapar ve derin öğrenme ile backlog'u önceliklendirir."""
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

        # Model eğitimi için veri toplama
        self._collect_training_data(created_sprint, prioritization)

        return {
            "sprint": created_sprint,
            "prioritization": prioritization
        }

    async def analyze_sprint_performance(self, sprint_id: int) -> Dict[str, Any]:
        """Sprint performansını derin öğrenme ile analiz eder."""
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

        # Model eğitimi için veri toplama
        self._collect_training_data(sprint, performance)

        return performance

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

        # Derin öğrenme ile rapor oluşturma
        report = {
            "sprint_summary": sprint.dict(),
            "performance_analysis": performance,
            "stakeholder_feedback": {
                "feedbacks": [f.dict() for f in feedbacks],
                "stakeholders": [s.dict() for s in stakeholders]
            },
            "agent_recommendations": performance["agent_recommendation"],
            "future_predictions": performance.get("future_predictions", {})
        }

        return report

    async def update_story_status(self, story_id: int, new_status: str) -> UserStory:
        """User story durumunu günceller ve derin öğrenme ile analiz eder."""
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

    def _collect_training_data(self, entity: Any, analysis: Dict[str, Any]):
        """Model eğitimi için veri toplar."""
        if isinstance(entity, UserStory):
            self.ai_agent.learning_history["story_embeddings"].append({
                "text": entity.description,
                "complexity": [
                    entity.complexity,
                    entity.business_value,
                    entity.risk_level
                ]
            })
        elif isinstance(entity, Sprint):
            self.ai_agent.learning_history["velocity_predictions"].append({
                "features": analysis["performance_metrics"],
                "points": entity.velocity
            })
            self.ai_agent.learning_history["agent_actions"].append({
                "state": analysis["performance_metrics"],
                "action": analysis["agent_recommendation"]
            })

    async def train_models(self):
        """Modelleri eğitir."""
        training_data = {
            "stories": self.ai_agent.learning_history["story_embeddings"],
            "velocities": self.ai_agent.learning_history["velocity_predictions"],
            "risks": self.ai_agent.learning_history["risk_assessments"],
            "actions": self.ai_agent.learning_history["agent_actions"]
        }
        self.ai_agent.train_models(training_data) 