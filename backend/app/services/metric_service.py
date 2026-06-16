from app.models.metric import Metric
from app.database.db import SessionLocal


def save_metric(
    server_id,
    cpu,
    ram,
    disk
):

    db = SessionLocal()

    try:

        metric = Metric(
            server_id=server_id,
            cpu=cpu,
            ram=ram,
            disk=disk
        )

        db.add(metric)

        db.commit()

        db.refresh(metric)

        return metric.id

    finally:

        db.close()


def get_all_metrics():

    db = SessionLocal()

    try:

        metrics = db.query(Metric).all()

        result = []

        for metric in metrics:

            result.append(
                {
                    "id": metric.id,
                    "server_id": metric.server_id,
                    "cpu": metric.cpu,
                    "ram": metric.ram,
                    "disk": metric.disk,
                    "created_at": str(metric.created_at)
                }
            )

        return result

    finally:

        db.close()


def get_latest_metric():

    db = SessionLocal()

    try:

        metric = (
            db.query(Metric)
            .order_by(Metric.id.desc())
            .first()
        )

        if not metric:

            return {
                "message": "No metrics found"
            }

        return {
            "id": metric.id,
            "server_id": metric.server_id,
            "cpu": metric.cpu,
            "ram": metric.ram,
            "disk": metric.disk,
            "created_at": str(metric.created_at)
        }

    finally:

        db.close()