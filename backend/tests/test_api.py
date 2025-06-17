import pytest
from fastapi.testclient import TestClient

def test_create_user_story(client, test_project):
    """User story oluşturma testi."""
    response = client.post(
        "/api/user-stories/",
        json={
            "title": "Test User Story",
            "description": "As a user, I want to test the API so that I can verify it works.",
            "project_id": test_project.id,
            "priority": "high",
            "story_points": 5
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test User Story"
    assert data["project_id"] == test_project.id

def test_get_user_stories(client, test_project):
    """User story listesi alma testi."""
    response = client.get(f"/api/user-stories/?project_id={test_project.id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_sprint(client, test_project):
    """Sprint oluşturma testi."""
    response = client.post(
        "/api/sprints/",
        json={
            "name": "Test Sprint",
            "start_date": "2024-01-01",
            "end_date": "2024-01-14",
            "project_id": test_project.id
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Sprint"
    assert data["project_id"] == test_project.id

def test_get_sprints(client, test_project):
    """Sprint listesi alma testi."""
    response = client.get(f"/api/sprints/?project_id={test_project.id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_task(client, test_sprint):
    """Task oluşturma testi."""
    response = client.post(
        "/api/tasks/",
        json={
            "title": "Test Task",
            "description": "Test task description",
            "story_points": 5,
            "sprint_id": test_sprint.id
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["sprint_id"] == test_sprint.id

def test_get_tasks(client, test_sprint):
    """Task listesi alma testi."""
    response = client.get(f"/api/tasks/?sprint_id={test_sprint.id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_analyze_user_story_ai(client):
    """AI user story analizi testi."""
    response = client.post(
        "/api/ai/analyze-user-story",
        json={
            "user_story": "As a user, I want to be able to reset my password so that I can access my account if I forget my password."
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "analysis" in data
    assert "story_points" in data

def test_prioritize_backlog_ai(client):
    """AI backlog önceliklendirme testi."""
    response = client.post(
        "/api/ai/prioritize-backlog",
        json={
            "backlog_items": [
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
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert all("priority" in item for item in data)

def test_analyze_sprint_velocity_ai(client):
    """AI sprint velocity analizi testi."""
    response = client.post(
        "/api/ai/analyze-sprint-velocity",
        json={
            "sprint_number": 1,
            "planned_story_points": 30,
            "completed_story_points": 25,
            "team_size": 5,
            "sprint_duration": 14
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "velocity" in data
    assert "trend" in data
    assert "recommendations" in data

def test_generate_sprint_report_ai(client):
    """AI sprint raporu oluşturma testi."""
    response = client.post(
        "/api/ai/generate-sprint-report",
        json={
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
    )
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "achievements" in data
    assert "challenges" in data
    assert "recommendations" in data 