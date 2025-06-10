from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
from app.core.services.deep_learning_ai_service import DeepLearningAIProductOwner
from app.core.services.business_intelligence_service import BusinessIntelligenceService
from app.core.services.team_management_service import TeamManagementService
from app.core.services.project_management_service import ProjectManagementService

class ReportingService:
    """Detaylı raporlama servisi"""

    def __init__(
        self,
        ai_service: DeepLearningAIProductOwner,
        bi_service: BusinessIntelligenceService,
        team_service: TeamManagementService,
        project_service: ProjectManagementService
    ):
        self.ai_service = ai_service
        self.bi_service = bi_service
        self.team_service = team_service
        self.project_service = project_service

    async def generate_comprehensive_report(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Kapsamlı proje raporu oluşturur."""
        # Proje sağlığı
        health_report = await self._generate_health_report(project_data)
        
        # Ekip performansı
        team_report = await self._generate_team_report(project_data)
        
        # İş metrikleri
        business_report = await self._generate_business_report(project_data)
        
        # Risk analizi
        risk_report = await self._generate_risk_report(project_data)
        
        # Öneriler ve iyileştirmeler
        recommendations = await self._generate_recommendations(project_data)
        
        return {
            "report_metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "project_id": project_data.get("id"),
                "report_type": "comprehensive"
            },
            "health_report": health_report,
            "team_report": team_report,
            "business_report": business_report,
            "risk_report": risk_report,
            "recommendations": recommendations
        }

    async def generate_sprint_report(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint raporu oluşturur."""
        # Sprint metrikleri
        sprint_metrics = await self._calculate_sprint_metrics(sprint_data)
        
        # Ekip performansı
        team_performance = await self._analyze_team_performance(sprint_data)
        
        # Kalite metrikleri
        quality_metrics = await self._analyze_quality_metrics(sprint_data)
        
        # Öğrenilen dersler
        lessons_learned = await self._analyze_lessons_learned(sprint_data)
        
        return {
            "report_metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "sprint_id": sprint_data.get("id"),
                "report_type": "sprint"
            },
            "sprint_metrics": sprint_metrics,
            "team_performance": team_performance,
            "quality_metrics": quality_metrics,
            "lessons_learned": lessons_learned
        }

    async def generate_team_report(self, team_data: Dict[str, Any]) -> Dict[str, Any]:
        """Ekip raporu oluşturur."""
        # Performans metrikleri
        performance = await self.team_service.analyze_team_performance(team_data)
        
        # Yetenek analizi
        skills = await self.team_service.match_skills_to_tasks(team_data, [])
        
        # Motivasyon analizi
        motivation = await self.team_service.analyze_team_motivation(team_data)
        
        # Eğitim ihtiyaçları
        training = await self.team_service.analyze_training_needs(team_data)
        
        return {
            "report_metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "team_id": team_data.get("id"),
                "report_type": "team"
            },
            "performance_analysis": performance,
            "skill_analysis": skills,
            "motivation_analysis": motivation,
            "training_analysis": training
        }

    async def generate_business_report(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """İş raporu oluşturur."""
        # Pazar analizi
        market_analysis = await self.bi_service.analyze_market_trends(project_data)
        
        # ROI analizi
        roi_analysis = await self.bi_service.calculate_roi(project_data)
        
        # Proje sağlığı
        project_health = await self.bi_service.analyze_project_health(project_data)
        
        return {
            "report_metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "project_id": project_data.get("id"),
                "report_type": "business"
            },
            "market_analysis": market_analysis,
            "roi_analysis": roi_analysis,
            "project_health": project_health
        }

    async def _generate_health_report(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sağlık raporu oluşturur."""
        health_metrics = await self.project_service.calculate_project_health(project_data)
        return {
            "metrics": health_metrics["health_metrics"],
            "trends": health_metrics["trend_analysis"],
            "risks": health_metrics["risk_assessment"],
            "improvements": health_metrics["improvements"]
        }

    async def _generate_team_report(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Ekip raporu oluşturur."""
        team_performance = await self.team_service.analyze_team_performance(project_data)
        return {
            "performance": team_performance["performance_metrics"],
            "skills": team_performance["skill_analysis"],
            "motivation": team_performance["motivation_analysis"],
            "improvements": team_performance["improvement_recommendations"]
        }

    async def _generate_business_report(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """İş raporu oluşturur."""
        market_trends = await self.bi_service.analyze_market_trends(project_data)
        roi = await self.bi_service.calculate_roi(project_data)
        return {
            "market_analysis": market_trends,
            "roi_analysis": roi,
            "recommendations": self._combine_recommendations(market_trends, roi)
        }

    async def _generate_risk_report(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Risk raporu oluşturur."""
        health_metrics = await self.project_service.calculate_project_health(project_data)
        team_performance = await self.team_service.analyze_team_performance(project_data)
        return {
            "project_risks": health_metrics["risk_assessment"],
            "team_risks": team_performance.get("risk_assessment", []),
            "mitigation_strategies": self._generate_mitigation_strategies(health_metrics, team_performance)
        }

    async def _generate_recommendations(self, project_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Öneriler oluşturur."""
        health_metrics = await self.project_service.calculate_project_health(project_data)
        team_performance = await self.team_service.analyze_team_performance(project_data)
        market_trends = await self.bi_service.analyze_market_trends(project_data)
        
        return self._combine_recommendations(
            health_metrics["improvements"],
            team_performance["improvement_recommendations"],
            market_trends["recommendations"]
        )

    async def _calculate_sprint_metrics(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint metriklerini hesaplar."""
        return {
            "velocity": 0.0,
            "story_points_completed": 0,
            "story_points_planned": 0,
            "completion_rate": 0.0,
            "quality_metrics": {}
        }

    async def _analyze_team_performance(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Ekip performansını analiz eder."""
        return {
            "velocity": 0.0,
            "quality_score": 0.0,
            "collaboration_score": 0.0,
            "improvement_areas": []
        }

    async def _analyze_quality_metrics(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Kalite metriklerini analiz eder."""
        return {
            "code_quality": 0.0,
            "test_coverage": 0.0,
            "bug_rate": 0.0,
            "technical_debt": 0.0
        }

    async def _analyze_lessons_learned(self, sprint_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Öğrenilen dersleri analiz eder."""
        return []

    def _combine_recommendations(self, *recommendation_sets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Önerileri birleştirir."""
        combined = []
        for recommendations in recommendation_sets:
            if recommendations:
                combined.extend(recommendations)
        return combined

    def _generate_mitigation_strategies(self, health_metrics: Dict[str, Any], team_performance: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Risk azaltma stratejileri oluşturur."""
        return [] 