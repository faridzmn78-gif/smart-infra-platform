from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_system_health():

    response = client.get("/system/health")

    assert response.status_code == 200

    data = response.json()

    assert "status" in data