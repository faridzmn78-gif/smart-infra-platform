from app.database.db import SessionLocal
from app.models.ml_prediction import MLPrediction


def save_ml_prediction(
    metric_id,
    prediction
):

    db = SessionLocal()

    try:

        ml_prediction = MLPrediction(
            metric_id=metric_id,
            prediction=prediction
        )

        db.add(ml_prediction)

        db.commit()

    finally:

        db.close()


def get_all_ml_predictions():

    db = SessionLocal()

    try:

        predictions = (
            db.query(MLPrediction)
            .all()
        )

        result = []

        for prediction in predictions:

            result.append(
                {
                    "id": prediction.id,
                    "metric_id": prediction.metric_id,
                    "prediction": prediction.prediction
                }
            )

        return result

    finally:

        db.close()


def get_latest_ml_prediction():

    db = SessionLocal()

    try:

        prediction = (
            db.query(MLPrediction)
            .order_by(
                MLPrediction.id.desc()
            )
            .first()
        )

        if not prediction:

            return {
                "message": "No predictions found"
            }

        return {
            "id": prediction.id,
            "metric_id": prediction.metric_id,
            "prediction": prediction.prediction
        }

    finally:

        db.close()