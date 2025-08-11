from app.main import app
from tests.custom_test_client import CustomTestClient

client = CustomTestClient(app)


def test_create_user():
    payload = {"name": "Alice", "email": "alice@example.com"}
    response = client.post("/api/users/", json=payload)
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data


def test_get_existing_user():
    payload = {"name": "Bob", "email": "bob@example.com"}
    post_resp = client.post("/api/users/", json=payload)
    user_id = post_resp.json()["id"]

    get_resp = client.get(f"/api/users/{user_id}")
    data = get_resp.json()
    assert data["name"] == "Bob"
    assert data["email"] == "bob@example.com"
    assert data["id"] == user_id


def test_get_nonexistent_user():
    response = client.get("/api/users/999", expected_status=404)
    assert response.json()["detail"] == "User not found"
