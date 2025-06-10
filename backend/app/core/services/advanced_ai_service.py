from typing import List, Dict, Any, Optional
import openai
from datetime import datetime
import json
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from app.core.config import settings
from app.core.domain.entities import UserStory, Sprint, ProductBacklog, Feedback

class AdvancedAIProductOwner:
    """Gelişmiş AI Product Owner - Makine öğrenmesi ve derin öğrenme yetenekleri ile donatılmış"""

    def __init__(self):
        self.model = "gpt-4"
        self.velocity_predictor = RandomForestRegressor()
        self.openai.api_key = settings.OPENAI_API_KEY
        
        # AI sistem promptu
        self.system_prompt = """You are an expert Product Owner with extensive experience in:
        - Advanced Agile/Scrum methodologies
        - Product management and strategy
        - Team leadership and coaching
        - Stakeholder management and communication
        - Technical project management
        - Risk assessment and mitigation
        - Performance analysis and optimization
        - Market analysis and competitive intelligence
        - User experience and design thinking
        - Data-driven decision making
        Your responses should be professional, data-driven, actionable, and backed by industry best practices."""

        # Öğrenme ve analiz geçmişi
        self.learning_history = {
            "velocity_trends": [],
            "story_complexity": {},
            "team_performance": {},
            "risk_patterns": {},
            "success_metrics": {}
        }

    async def analyze_user_story(self, story: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """User story'yi gelişmiş analiz teknikleri ile değerlendirir."""
        # NLP analizi
        nlp_analysis = await self._perform_nlp_analysis(story)
        
        # Karmaşıklık analizi
        complexity_analysis = self._analyze_complexity(story, context)
        
        # Risk analizi
        risk_analysis = await self._analyze_risks(story, context)
        
        # Değer analizi
        value_analysis = await self._analyze_business_value(story, context)
        
        # Story point tahmini
        story_points = self._predict_story_points(
            nlp_analysis,
            complexity_analysis,
            risk_analysis,
            value_analysis
        )

        return {
            "nlp_analysis": nlp_analysis,
            "complexity_analysis": complexity_analysis,
            "risk_analysis": risk_analysis,
            "value_analysis": value_analysis,
            "story_points": story_points,
            "recommendations": self._generate_recommendations(
                nlp_analysis,
                complexity_analysis,
                risk_analysis,
                value_analysis
            )
        }

    async def prioritize_backlog(self, items: List[Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Backlog öğelerini gelişmiş önceliklendirme algoritmaları ile değerlendirir."""
        # Değer analizi
        value_scores = await self._analyze_items_value(items, context)
        
        # Risk analizi
        risk_scores = await self._analyze_items_risk(items, context)
        
        # Bağımlılık analizi
        dependency_graph = self._analyze_dependencies(items)
        
        # Kaynak analizi
        resource_analysis = self._analyze_resource_requirements(items, context)
        
        # Önceliklendirme
        prioritization = self._calculate_priorities(
            value_scores,
            risk_scores,
            dependency_graph,
            resource_analysis
        )

        return {
            "prioritized_items": prioritization,
            "value_analysis": value_scores,
            "risk_analysis": risk_scores,
            "dependency_analysis": dependency_graph,
            "resource_analysis": resource_analysis,
            "recommendations": self._generate_prioritization_recommendations(
                prioritization,
                value_scores,
                risk_scores,
                dependency_graph,
                resource_analysis
            )
        }

    async def analyze_sprint_performance(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint performansını gelişmiş analiz teknikleri ile değerlendirir."""
        # Velocity analizi
        velocity_analysis = self._analyze_velocity_trends(sprint_data)
        
        # Takım performans analizi
        team_performance = self._analyze_team_performance(sprint_data)
        
        # Kalite analizi
        quality_metrics = self._analyze_quality_metrics(sprint_data)
        
        # Risk analizi
        risk_assessment = self._analyze_sprint_risks(sprint_data)
        
        # Süreç analizi
        process_analysis = self._analyze_process_efficiency(sprint_data)

        return {
            "velocity_analysis": velocity_analysis,
            "team_performance": team_performance,
            "quality_metrics": quality_metrics,
            "risk_assessment": risk_assessment,
            "process_analysis": process_analysis,
            "recommendations": self._generate_performance_recommendations(
                velocity_analysis,
                team_performance,
                quality_metrics,
                risk_assessment,
                process_analysis
            )
        }

    async def predict_future_performance(self, historical_data: Dict[str, Any]) -> Dict[str, Any]:
        """Gelecek performansı makine öğrenmesi ile tahmin eder."""
        # Veri hazırlama
        features = self._prepare_prediction_features(historical_data)
        
        # Model eğitimi
        self._train_prediction_models(features)
        
        # Tahminler
        velocity_prediction = self._predict_velocity(features)
        risk_prediction = self._predict_risks(features)
        quality_prediction = self._predict_quality(features)
        
        return {
            "velocity_prediction": velocity_prediction,
            "risk_prediction": risk_prediction,
            "quality_prediction": quality_prediction,
            "confidence_scores": self._calculate_prediction_confidence(),
            "recommendations": self._generate_prediction_recommendations(
                velocity_prediction,
                risk_prediction,
                quality_prediction
            )
        }

    async def _perform_nlp_analysis(self, text: str) -> Dict[str, Any]:
        """Doğal dil işleme analizi yapar."""
        prompt = f"""
        Perform a detailed NLP analysis of the following text:
        {text}

        Analyze:
        1. Semantic meaning
        2. Key concepts
        3. Action items
        4. Dependencies
        5. Technical terms
        6. Business value indicators
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_nlp_analysis(response)

    def _analyze_complexity(self, story: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Karmaşıklık analizi yapar."""
        # Karmaşıklık faktörlerini analiz et
        technical_complexity = self._analyze_technical_complexity(story)
        business_complexity = self._analyze_business_complexity(story)
        integration_complexity = self._analyze_integration_complexity(story, context)
        
        return {
            "technical_complexity": technical_complexity,
            "business_complexity": business_complexity,
            "integration_complexity": integration_complexity,
            "total_complexity": self._calculate_total_complexity(
                technical_complexity,
                business_complexity,
                integration_complexity
            )
        }

    async def _analyze_risks(self, story: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Risk analizi yapar."""
        prompt = f"""
        Analyze potential risks in the following user story:
        {story}

        Consider:
        1. Technical risks
        2. Business risks
        3. Resource risks
        4. Timeline risks
        5. Integration risks
        6. Market risks
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_risk_analysis(response)

    async def _analyze_business_value(self, story: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """İş değeri analizi yapar."""
        prompt = f"""
        Analyze the business value of the following user story:
        {story}

        Consider:
        1. Revenue impact
        2. Customer satisfaction
        3. Market positioning
        4. Strategic alignment
        5. Competitive advantage
        6. Long-term value
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_value_analysis(response)

    def _predict_story_points(
        self,
        nlp_analysis: Dict[str, Any],
        complexity_analysis: Dict[str, Any],
        risk_analysis: Dict[str, Any],
        value_analysis: Dict[str, Any]
    ) -> int:
        """Story point tahmini yapar."""
        # Özellik vektörü oluştur
        features = self._create_story_point_features(
            nlp_analysis,
            complexity_analysis,
            risk_analysis,
            value_analysis
        )
        
        # Tahmin yap
        prediction = self.velocity_predictor.predict([features])[0]
        
        # Tahmini yuvarla
        return round(prediction)

    def _analyze_velocity_trends(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Velocity trendlerini analiz eder."""
        # Velocity verilerini hazırla
        velocity_data = self._prepare_velocity_data(sprint_data)
        
        # Trend analizi yap
        trend = self._calculate_velocity_trend(velocity_data)
        
        # Anomali tespiti
        anomalies = self._detect_velocity_anomalies(velocity_data)
        
        return {
            "current_velocity": velocity_data[-1],
            "trend": trend,
            "anomalies": anomalies,
            "forecast": self._forecast_velocity(velocity_data)
        }

    def _analyze_team_performance(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Takım performansını analiz eder."""
        # Performans metriklerini hesapla
        metrics = self._calculate_team_metrics(sprint_data)
        
        # Trend analizi
        trends = self._analyze_performance_trends(metrics)
        
        # İyileştirme alanları
        improvements = self._identify_improvement_areas(metrics)
        
        return {
            "metrics": metrics,
            "trends": trends,
            "improvements": improvements,
            "recommendations": self._generate_team_recommendations(metrics, trends)
        }

    async def _get_ai_response(self, prompt: str) -> str:
        """AI modelinden yanıt alır."""
        try:
            response = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"AI model error: {str(e)}")

    def _update_learning_history(self, new_data: Dict[str, Any]):
        """Öğrenme geçmişini günceller."""
        for key, value in new_data.items():
            if key in self.learning_history:
                self.learning_history[key].append(value)
                
                # Geçmiş verileri optimize et
                if len(self.learning_history[key]) > 1000:
                    self.learning_history[key] = self.learning_history[key][-1000:] 