from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_user():
    payload = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/api/users/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data


def test_get_existing_user():
    payload = {"name": "Bob", "email": "bob@example.com"}
    post_resp = client.post("/api/users/", json=payload)
    user_id = post_resp.json()["id"]

    get_resp = client.get(f"/api/users/{user_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["name"] == "Bob"
    assert data["email"] == "bob@example.com"
    assert data["id"] == user_id


def test_get_nonexistent_user():
    response = client.get("/api/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
