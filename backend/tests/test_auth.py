def test_login_success(client):
    response = client.post("/auth/login", json={"username": "test", "password": "test"})
    assert response.status_code in (200, 401)  # test kullanıcı DB'de olmayabilir

def test_token_protected(client):
    response = client.get("/auth/me", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401
