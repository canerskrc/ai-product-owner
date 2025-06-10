from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json
from app.core.services.reporting_service import ReportingService

class VisualizationService:
    """Görselleştirme servisi"""

    def __init__(self, reporting_service: ReportingService):
        self.reporting_service = reporting_service
        self.color_palette = px.colors.qualitative.Set3

    async def create_dashboard(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Proje dashboard'u oluşturur."""
        # Kapsamlı rapor al
        report = await self.reporting_service.generate_comprehensive_report(project_data)
        
        # Dashboard bileşenleri
        components = {
            "project_health": await self._create_health_dashboard(report["health_report"]),
            "team_performance": await self._create_team_dashboard(report["team_report"]),
            "business_metrics": await self._create_business_dashboard(report["business_report"]),
            "risk_analysis": await self._create_risk_dashboard(report["risk_report"]),
            "recommendations": await self._create_recommendations_dashboard(report["recommendations"])
        }
        
        return {
            "dashboard_metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "project_id": project_data.get("id"),
                "dashboard_type": "comprehensive"
            },
            "components": components
        }

    async def create_sprint_visualization(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint görselleştirmesi oluşturur."""
        # Sprint raporu al
        report = await self.reporting_service.generate_sprint_report(sprint_data)
        
        # Görselleştirmeler
        visualizations = {
            "velocity_chart": await self._create_velocity_chart(report["sprint_metrics"]),
            "quality_metrics": await self._create_quality_metrics_chart(report["quality_metrics"]),
            "team_performance": await self._create_team_performance_chart(report["team_performance"]),
            "lessons_learned": await self._create_lessons_learned_chart(report["lessons_learned"])
        }
        
        return {
            "visualization_metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "sprint_id": sprint_data.get("id"),
                "visualization_type": "sprint"
            },
            "visualizations": visualizations
        }

    async def _create_health_dashboard(self, health_report: Dict[str, Any]) -> Dict[str, Any]:
        """Sağlık dashboard'u oluşturur."""
        metrics = health_report["metrics"]
        trends = health_report["trends"]
        
        return {
            "health_radar": self._create_radar_chart(metrics),
            "trend_line": self._create_trend_line(trends),
            "risk_heatmap": self._create_risk_heatmap(health_report["risks"]),
            "improvement_gauge": self._create_improvement_gauge(metrics)
        }

    async def _create_team_dashboard(self, team_report: Dict[str, Any]) -> Dict[str, Any]:
        """Ekip dashboard'u oluşturur."""
        performance = team_report["performance"]
        skills = team_report["skills"]
        
        return {
            "performance_radar": self._create_radar_chart(performance),
            "skill_matrix": self._create_skill_matrix(skills),
            "motivation_chart": self._create_motivation_chart(team_report["motivation"]),
            "improvement_timeline": self._create_improvement_timeline(team_report["improvements"])
        }

    async def _create_business_dashboard(self, business_report: Dict[str, Any]) -> Dict[str, Any]:
        """İş dashboard'u oluşturur."""
        market = business_report["market_analysis"]
        roi = business_report["roi_analysis"]
        
        return {
            "market_trends": self._create_market_trends_chart(market),
            "roi_chart": self._create_roi_chart(roi),
            "project_health": self._create_project_health_chart(business_report["project_health"]),
            "recommendations": self._create_recommendations_chart(business_report["recommendations"])
        }

    async def _create_risk_dashboard(self, risk_report: Dict[str, Any]) -> Dict[str, Any]:
        """Risk dashboard'u oluşturur."""
        return {
            "risk_matrix": self._create_risk_matrix(risk_report["project_risks"]),
            "team_risk_chart": self._create_team_risk_chart(risk_report["team_risks"]),
            "mitigation_strategies": self._create_mitigation_chart(risk_report["mitigation_strategies"])
        }

    def _create_radar_chart(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Radar chart oluşturur."""
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=list(data.values()),
            theta=list(data.keys()),
            fill='toself',
            name='Metrics'
        ))
        return fig.to_json()

    def _create_trend_line(self, trends: Dict[str, Any]) -> Dict[str, Any]:
        """Trend çizgisi oluşturur."""
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=list(trends.keys()),
            y=list(trends.values()),
            mode='lines+markers',
            name='Trend'
        ))
        return fig.to_json()

    def _create_risk_heatmap(self, risks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Risk ısı haritası oluşturur."""
        fig = go.Figure(data=go.Heatmap(
            z=[[risk.get("probability", 0), risk.get("impact", 0)] for risk in risks],
            colorscale='Reds'
        ))
        return fig.to_json()

    def _create_improvement_gauge(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """İyileştirme göstergesi oluşturur."""
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=metrics.get("overall_health", 0),
            title={'text': "Overall Health"},
            gauge={'axis': {'range': [0, 100]}}
        ))
        return fig.to_json()

    def _create_skill_matrix(self, skills: Dict[str, Any]) -> Dict[str, Any]:
        """Yetenek matrisi oluşturur."""
        fig = go.Figure(data=go.Heatmap(
            z=[[skill.get("level", 0) for skill in skills.values()]],
            colorscale='Viridis'
        ))
        return fig.to_json()

    def _create_motivation_chart(self, motivation: Dict[str, Any]) -> Dict[str, Any]:
        """Motivasyon grafiği oluşturur."""
        fig = go.Figure(data=[
            go.Bar(
                x=list(motivation.keys()),
                y=list(motivation.values()),
                marker_color=self.color_palette
            )
        ])
        return fig.to_json()

    def _create_improvement_timeline(self, improvements: List[Dict[str, Any]]) -> Dict[str, Any]:
        """İyileştirme zaman çizelgesi oluşturur."""
        fig = go.Figure(data=[
            go.Scatter(
                x=[imp.get("date", "") for imp in improvements],
                y=[imp.get("impact", 0) for imp in improvements],
                mode='lines+markers',
                name='Improvements'
            )
        ])
        return fig.to_json()

    def _create_market_trends_chart(self, market: Dict[str, Any]) -> Dict[str, Any]:
        """Pazar trendleri grafiği oluşturur."""
        fig = go.Figure()
        for trend in market.get("trends", []):
            fig.add_trace(go.Scatter(
                x=trend.get("dates", []),
                y=trend.get("values", []),
                name=trend.get("name", "")
            ))
        return fig.to_json()

    def _create_roi_chart(self, roi: Dict[str, Any]) -> Dict[str, Any]:
        """ROI grafiği oluşturur."""
        fig = go.Figure(data=[
            go.Bar(
                x=["ROI", "Payback Period", "NPV", "IRR"],
                y=[
                    roi.get("roi", 0),
                    roi.get("payback_period", 0),
                    roi.get("npv", 0),
                    roi.get("irr", 0)
                ],
                marker_color=self.color_palette
            )
        ])
        return fig.to_json()

    def _create_project_health_chart(self, health: Dict[str, Any]) -> Dict[str, Any]:
        """Proje sağlığı grafiği oluşturur."""
        fig = go.Figure(data=[
            go.Indicator(
                mode="gauge+number",
                value=health.get("overall_health", 0),
                title={'text': "Project Health"},
                gauge={'axis': {'range': [0, 100]}}
            )
        ])
        return fig.to_json()

    def _create_recommendations_chart(self, recommendations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Öneriler grafiği oluşturur."""
        fig = go.Figure(data=[
            go.Bar(
                x=[rec.get("category", "") for rec in recommendations],
                y=[rec.get("impact", 0) for rec in recommendations],
                marker_color=self.color_palette
            )
        ])
        return fig.to_json()

    def _create_risk_matrix(self, risks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Risk matrisi oluşturur."""
        fig = go.Figure(data=go.Scatter(
            x=[risk.get("probability", 0) for risk in risks],
            y=[risk.get("impact", 0) for risk in risks],
            mode='markers',
            marker=dict(
                size=[risk.get("severity", 1) * 10 for risk in risks],
                color=[risk.get("severity", 1) for risk in risks],
                colorscale='Reds'
            )
        ))
        return fig.to_json()

    def _create_team_risk_chart(self, risks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Ekip risk grafiği oluşturur."""
        fig = go.Figure(data=[
            go.Bar(
                x=[risk.get("category", "") for risk in risks],
                y=[risk.get("severity", 0) for risk in risks],
                marker_color=self.color_palette
            )
        ])
        return fig.to_json()

    def _create_mitigation_chart(self, strategies: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Risk azaltma stratejileri grafiği oluşturur."""
        fig = go.Figure(data=[
            go.Bar(
                x=[strategy.get("category", "") for strategy in strategies],
                y=[strategy.get("effectiveness", 0) for strategy in strategies],
                marker_color=self.color_palette
            )
        ])
        return fig.to_json() 