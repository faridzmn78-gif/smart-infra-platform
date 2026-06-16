from app.models.anomaly import Anomaly
from app.database.db import SessionLocal


def detect_anomaly(cpu, ram, disk):

    result = {
        "cpu_status": "normal",
        "ram_status": "normal",
        "disk_status": "normal"
    }

    if cpu > 80:
        result["cpu_status"] = "anomaly"

    if ram > 85:
        result["ram_status"] = "anomaly"

    if disk > 90:
        result["disk_status"] = "anomaly"

    return result


def save_anomaly(
    metric_id,
    cpu_status,
    ram_status,
    disk_status
):

    db = SessionLocal()

    try:

        anomaly = Anomaly(
            metric_id=metric_id,
            cpu_status=cpu_status,
            ram_status=ram_status,
            disk_status=disk_status
        )

        db.add(anomaly)

        db.commit()

    finally:

        db.close()


def get_all_anomalies():

    db = SessionLocal()

    try:

        anomalies = db.query(Anomaly).all()

        result = []

        for anomaly in anomalies:

            result.append(
                {
                    "id": anomaly.id,
                    "metric_id": anomaly.metric_id,
                    "cpu_status": anomaly.cpu_status,
                    "ram_status": anomaly.ram_status,
                    "disk_status": anomaly.disk_status
                }
            )

        return result

    finally:

        db.close()


def get_latest_anomaly():

    db = SessionLocal()

    try:

        anomaly = (
            db.query(Anomaly)
            .order_by(Anomaly.id.desc())
            .first()
        )

        if not anomaly:

            return {
                "message": "No anomalies found"
            }

        return {
            "id": anomaly.id,
            "metric_id": anomaly.metric_id,
            "cpu_status": anomaly.cpu_status,
            "ram_status": anomaly.ram_status,
            "disk_status": anomaly.disk_status
        }

    finally:

        db.close()


def get_system_health():

    latest = get_latest_anomaly()

    if "message" in latest:
        return {
            "status": "unknown"
        }

    overall_status = "healthy"

    if (
        latest["cpu_status"] == "anomaly"
        or latest["ram_status"] == "anomaly"
        or latest["disk_status"] == "anomaly"
    ):
        overall_status = "warning"

    return {
        "status": overall_status,
        "latest_metric_id": latest["metric_id"],
        "cpu_status": latest["cpu_status"],
        "ram_status": latest["ram_status"],
        "disk_status": latest["disk_status"]
    }