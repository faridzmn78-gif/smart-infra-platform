from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_latest_prediction():

    response = client.get("/ml-predictions/latest")

    assert response.status_code == 200


def test_predictions():

    response = client.get("/ml-predictions")

    assert response.status_code == 200