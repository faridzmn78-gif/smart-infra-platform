from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_latest_metric():

    response = client.get("/metrics/latest")

    assert response.status_code == 200


def test_metrics():

    response = client.get("/metrics")

    assert response.status_code == 200