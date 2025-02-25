from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_add_requirement():
    requirement_data = {
        "title": "Dark mode support",
        "description": "Add dark mode to the application"
    }
    response = client.post("/requirements", json=requirement_data)
    assert response.status_code == 200
    assert "id" in response.json()
    assert "priority" in response.json()

def test_list_requirements():
    response = client.get("/requirements")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_feedback():
    requirement_data = {
        "title": "Dark mode",
        "description": "User requests dark mode"
    }
    req_response = client.post("/requirements", json=requirement_data)
    requirement_id = req_response.json()["id"]

    feedback_data = {
        "requirement_id": requirement_id,
        "feedback_text": "This feature is essential for accessibility."
    }
    response = client.post("/feedback", json=feedback_data)
    assert response.status_code == 200
    assert response.json()["feedback_text"] == feedback_data["feedback_text"]

def test_get_feedback():
    requirement_data = {
        "title": "Dark mode",
        "description": "User requests dark mode"
    }
    req_response = client.post("/requirements", json=requirement_data)
    requirement_id = req_response.json()["id"]

    feedback_data = {
        "requirement_id": requirement_id,
        "feedback_text": "This feature is essential."
    }
    client.post("/feedback", json=feedback_data)

    response = client.get(f"/feedback/{requirement_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
