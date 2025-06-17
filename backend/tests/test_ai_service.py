import pytest
from app.core.services.ai_service import AIService

@pytest.fixture
def ai_service():
    return AIService()

def test_analyze_user_story(ai_service):
    """User story analizi testi."""
    user_story = "As a user, I want to be able to reset my password so that I can access my account if I forget my password."
    
    result = ai_service.analyze_user_story(user_story)
    
    assert result is not None
    assert "analysis" in result
    assert "story_points" in result
    assert isinstance(result["story_points"], int)
    assert result["story_points"] > 0

def test_prioritize_backlog(ai_service):
    """Backlog önceliklendirme testi."""
    backlog_items = [
        {
            "title": "User Authentication",
            "description": "Implement user authentication system",
            "business_value": 8,
            "technical_complexity": 7
        },
        {
            "title": "Password Reset",
            "description": "Implement password reset functionality",
            "business_value": 6,
            "technical_complexity": 5
        }
    ]
    
    result = ai_service.prioritize_backlog(backlog_items)
    
    assert result is not None
    assert len(result) == len(backlog_items)
    assert all("priority" in item for item in result)
    assert all("reason" in item for item in result)

def test_analyze_sprint_velocity(ai_service):
    """Sprint velocity analizi testi."""
    sprint_data = {
        "sprint_number": 1,
        "planned_story_points": 30,
        "completed_story_points": 25,
        "team_size": 5,
        "sprint_duration": 14
    }
    
    result = ai_service.analyze_sprint_velocity(sprint_data)
    
    assert result is not None
    assert "velocity" in result
    assert "trend" in result
    assert "recommendations" in result
    assert isinstance(result["velocity"], float)
    assert result["velocity"] > 0

def test_generate_sprint_report(ai_service):
    """Sprint raporu oluşturma testi."""
    sprint_data = {
        "sprint_number": 1,
        "start_date": "2024-01-01",
        "end_date": "2024-01-14",
        "completed_tasks": [
            {"title": "Task 1", "story_points": 5},
            {"title": "Task 2", "story_points": 3}
        ],
        "team_performance": {
            "velocity": 8,
            "quality_score": 0.85
        }
    }
    
    result = ai_service.generate_sprint_report(sprint_data)
    
    assert result is not None
    assert "summary" in result
    assert "achievements" in result
    assert "challenges" in result
    assert "recommendations" in result
    assert isinstance(result["summary"], str)
    assert len(result["achievements"]) > 0
    assert len(result["challenges"]) >= 0
    assert len(result["recommendations"]) > 0 