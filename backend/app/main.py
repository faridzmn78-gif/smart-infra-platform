from fastapi import FastAPI

from app.database.db import engine

from app.models.metric import Base

# Import all models so SQLAlchemy registers them
from app.models.server import Server
from app.models.anomaly import Anomaly
from app.models.ml_prediction import MLPrediction

from app.services.metric_service import (
    save_metric,
    get_all_metrics,
    get_latest_metric
)

from app.services.server_service import (
    get_or_create_server
)

from app.services.anomaly_service import (
    detect_anomaly,
    save_anomaly,
    get_all_anomalies,
    get_latest_anomaly,
    get_system_health
)

from app.services.ml_prediction_service import (
    get_all_ml_predictions,
    get_latest_ml_prediction
)

app = FastAPI()


@app.on_event("startup")
def startup():

    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():

    return {
        "status": "running",
        "project": "smart-infra-platform"
    }


@app.post("/metrics")
def receive_metrics(data: dict):

    server_id = get_or_create_server(
        hostname=data["hostname"],
        os=data["os"],
        os_version=data["os_version"]
    )

    metric_id = save_metric(
        server_id=server_id,
        cpu=data["cpu"],
        ram=data["ram"],
        disk=data["disk"]
    )

    anomaly_result = detect_anomaly(
        cpu=data["cpu"],
        ram=data["ram"],
        disk=data["disk"]
    )

    save_anomaly(
        metric_id=metric_id,
        cpu_status=anomaly_result["cpu_status"],
        ram_status=anomaly_result["ram_status"],
        disk_status=anomaly_result["disk_status"]
    )

    return {
        "message": "Metrics saved successfully",
        "server_id": server_id,
        "metric_id": metric_id,
        "anomaly_result": anomaly_result
    }


@app.get("/metrics")
def read_metrics():

    return get_all_metrics()


@app.get("/metrics/latest")
def read_latest_metric():

    return get_latest_metric()


@app.get("/anomalies")
def read_anomalies():

    return get_all_anomalies()


@app.get("/anomalies/latest")
def read_latest_anomaly_endpoint():

    return get_latest_anomaly()


@app.get("/system/health")
def system_health():

    return get_system_health()


@app.get("/ml-predictions")
def read_ml_predictions():

    return get_all_ml_predictions()


@app.get("/ml-predictions/latest")
def read_latest_ml_prediction():

    return get_latest_ml_prediction()