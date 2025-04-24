def test_generate_sprint_report(client):
    payload = {
        "team_data": {"alice": 3, "murat": 2},
        "issues": [
            {"title": "Refactor login", "status": "done", "assignee": "murat"}
        ],
        "historical_velocity": 6.0
    }
    response = client.post("/reports/sprint", json=payload)
    assert response.status_code == 200
    assert "report" in response.json()
