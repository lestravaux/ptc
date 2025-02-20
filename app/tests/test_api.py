import pytest
from fastapi.testclient import TestClient
from app.main import app
from database import Base, engine, SessionLocal

# Use an in-memory SQLite DB for testing
Base.metadata.create_all(bind=engine)
client = TestClient(app)

def test_create_user():
    response = client.post("/user", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert "id" in data

def test_get_users():
    # Ensure at least one user exists (created in previous test)
    response = client.get("/users")
    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "name" in data[0]
        assert "email" in data[0]
