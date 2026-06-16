from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_latest_anomaly():

    response = client.get("/anomalies/latest")

    assert response.status_code == 200


def test_anomalies():

    response = client.get("/anomalies")

    assert response.status_code == 200