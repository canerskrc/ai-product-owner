from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["username"] == user_data["username"]

def test_login():
    login_data = {
        "username": "testuser",
        "password": "securepassword"
    }
    response = client.post("/auth/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route():
    login_data = {
        "username": "testuser",
        "password": "securepassword"
    }
    login_response = client.post("/auth/token", data=login_data)
    token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/requirements", headers=headers)
    assert response.status_code == 200
