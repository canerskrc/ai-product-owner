def test_generate_tasks(client):
    response = client.post("/jira/tasks/generate", json={"feature_description": "Add dark mode to app"})
    assert response.status_code == 200
    assert "tasks" in response.json()
