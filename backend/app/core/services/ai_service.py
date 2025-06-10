from typing import List, Dict, Any, Optional
import openai
from datetime import datetime
import json
from app.core.config import settings
from app.core.domain.entities import UserStory, Sprint, ProductBacklog, Feedback

class AIProductOwnerAgent:
    """AI Product Owner Agent - Üst düzey ürün yönetimi ve analiz yetenekleri"""
    
    def __init__(self):
        self.model = "gpt-4"
        openai.api_key = settings.OPENAI_API_KEY
        self.system_prompt = """You are an expert Product Owner with extensive experience in:
        - Agile/Scrum methodologies
        - Product management
        - Team leadership
        - Stakeholder management
        - Technical project management
        - Risk assessment and mitigation
        - Performance analysis
        Your responses should be professional, data-driven, and actionable."""

    async def analyze_user_story(self, story: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """User story'yi kapsamlı analiz eder ve iyileştirme önerileri sunar."""
        prompt = f"""
        Analyze the following user story with the given context and provide a detailed assessment:

        User Story: {story}
        Context: {json.dumps(context) if context else 'No additional context provided'}

        Please provide:
        1. Clarity Assessment
           - Story completeness
           - Acceptance criteria quality
           - Dependencies identification
           - Risk factors

        2. Technical Analysis
           - Complexity estimation
           - Technical dependencies
           - Implementation considerations
           - Potential challenges

        3. Business Value Assessment
           - Value proposition
           - Stakeholder impact
           - ROI potential
           - Strategic alignment

        4. Recommendations
           - Story improvements
           - Acceptance criteria suggestions
           - Risk mitigation strategies
           - Implementation approach

        5. Story Point Estimation
           - Detailed breakdown
           - Confidence level
           - Assumptions
           - Historical comparison
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_story_analysis(response)

    async def prioritize_backlog(self, items: List[Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Backlog öğelerini kapsamlı kriterlere göre önceliklendirir."""
        prompt = f"""
        Prioritize the following backlog items considering all relevant factors:

        Backlog Items: {json.dumps(items)}
        Context: {json.dumps(context) if context else 'No additional context provided'}

        Consider:
        1. Business Value
           - Revenue impact
           - Customer satisfaction
           - Market positioning
           - Strategic alignment

        2. Technical Factors
           - Implementation complexity
           - Technical debt
           - Dependencies
           - Resource requirements

        3. Risk Assessment
           - Technical risks
           - Business risks
           - Market risks
           - Implementation risks

        4. Resource Constraints
           - Team capacity
           - Skill requirements
           - Timeline constraints
           - Budget considerations

        Provide:
        1. Prioritized list with justification
        2. Risk assessment for each item
        3. Resource allocation recommendations
        4. Timeline suggestions
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_prioritization(response)

    async def analyze_sprint_performance(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint performansını detaylı analiz eder ve öneriler sunar."""
        prompt = f"""
        Analyze the following sprint data and provide comprehensive insights:

        Sprint Data: {json.dumps(sprint_data)}

        Analyze:
        1. Team Performance
           - Velocity trends
           - Story point completion
           - Quality metrics
           - Team dynamics

        2. Process Efficiency
           - Sprint planning effectiveness
           - Daily scrum efficiency
           - Sprint review quality
           - Retrospective outcomes

        3. Risk Assessment
           - Identified risks
           - Risk mitigation effectiveness
           - New risk factors
           - Risk trends

        4. Improvement Opportunities
           - Process improvements
           - Team development needs
           - Technical improvements
           - Communication enhancements

        Provide:
        1. Detailed analysis
        2. Actionable recommendations
        3. Risk mitigation strategies
        4. Success metrics
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_sprint_analysis(response)

    async def generate_sprint_report(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Profesyonel sprint raporu oluşturur."""
        prompt = f"""
        Generate a comprehensive sprint report based on the following data:

        Sprint Data: {json.dumps(sprint_data)}

        Include:
        1. Executive Summary
           - Key achievements
           - Major challenges
           - Critical metrics
           - Strategic impact

        2. Detailed Analysis
           - Story completion analysis
           - Quality metrics
           - Team performance
           - Process effectiveness

        3. Risk Assessment
           - Current risks
           - Mitigation status
           - New risks identified
           - Risk trends

        4. Recommendations
           - Process improvements
           - Team development
           - Technical enhancements
           - Strategic adjustments

        5. Next Steps
           - Action items
           - Priority recommendations
           - Resource requirements
           - Timeline suggestions
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_sprint_report(response)

    async def analyze_stakeholder_feedback(self, feedback: List[Feedback]) -> Dict[str, Any]:
        """Stakeholder geri bildirimlerini analiz eder ve öneriler sunar."""
        prompt = f"""
        Analyze the following stakeholder feedback and provide insights:

        Feedback: {json.dumps([f.dict() for f in feedback])}

        Analyze:
        1. Feedback Patterns
           - Common themes
           - Priority areas
           - Stakeholder concerns
           - Positive feedback

        2. Impact Assessment
           - Business impact
           - Technical impact
           - Team impact
           - Process impact

        3. Action Items
           - Immediate actions
           - Long-term improvements
           - Communication needs
           - Resource requirements

        4. Risk Assessment
           - Stakeholder risks
           - Project risks
           - Team risks
           - Process risks
        """
        
        response = await self._get_ai_response(prompt)
        return self._parse_feedback_analysis(response)

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

    def _parse_story_analysis(self, analysis: str) -> Dict[str, Any]:
        """Story analiz sonucunu parse eder."""
        # Parse logic implementation
        return {
            "analysis": analysis,
            "story_points": self._estimate_story_points(analysis),
            "risks": self._extract_risks(analysis),
            "recommendations": self._extract_recommendations(analysis)
        }

    def _parse_prioritization(self, prioritization: str) -> Dict[str, Any]:
        """Önceliklendirme sonucunu parse eder."""
        # Parse logic implementation
        return {
            "prioritized_items": [],
            "risk_assessment": {},
            "resource_allocation": {},
            "timeline": {}
        }

    def _parse_sprint_analysis(self, analysis: str) -> Dict[str, Any]:
        """Sprint analiz sonucunu parse eder."""
        # Parse logic implementation
        return {
            "performance_metrics": {},
            "risk_assessment": {},
            "improvements": [],
            "success_metrics": {}
        }

    def _parse_sprint_report(self, report: str) -> Dict[str, Any]:
        """Sprint raporunu parse eder."""
        # Parse logic implementation
        return {
            "executive_summary": {},
            "detailed_analysis": {},
            "risk_assessment": {},
            "recommendations": [],
            "next_steps": []
        }

    def _parse_feedback_analysis(self, analysis: str) -> Dict[str, Any]:
        """Geri bildirim analizini parse eder."""
        # Parse logic implementation
        return {
            "patterns": {},
            "impact_assessment": {},
            "action_items": [],
            "risk_assessment": {}
        }

    def _estimate_story_points(self, analysis: str) -> int:
        """Story point tahmini yapar."""
        # Estimation logic implementation
        return 5

    def _extract_risks(self, analysis: str) -> List[Dict[str, Any]]:
        """Risk faktörlerini çıkarır."""
        # Risk extraction logic implementation
        return []

    def _extract_recommendations(self, analysis: str) -> List[str]:
        """Önerileri çıkarır."""
        # Recommendation extraction logic implementation
        return [] 