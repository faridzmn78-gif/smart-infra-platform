import os

import joblib
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy import text

DATABASE_URL = os.getenv(
"DATABASE_URL",
"postgresql://admin:admin123@postgres:5432/smart_infra"
)

MODEL_PATH = "model/isolation_forest.pkl"

engine = create_engine(DATABASE_URL)

def predict_and_save():

```
try:

    if not os.path.exists(
        MODEL_PATH
    ):

        print(
            "Model file not found"
        )

        return

    model = joblib.load(
        MODEL_PATH
    )

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT id, cpu, ram, disk
                FROM metrics
                ORDER BY id DESC
                LIMIT 1
                """
            )
        )

        metric = result.fetchone()

        if not metric:

            print(
                "No metrics found"
            )

            return

        metric_id = metric.id

        existing = conn.execute(
            text(
                """
                SELECT id
                FROM ml_predictions
                WHERE metric_id = :metric_id
                LIMIT 1
                """
            ),
            {
                "metric_id": metric_id
            }
        ).fetchone()

        if existing:

            print(
                f"Prediction already exists for metric {metric_id}"
            )

            return

        df = pd.DataFrame(
            [
                {
                    "cpu": metric.cpu,
                    "ram": metric.ram,
                    "disk": metric.disk
                }
            ]
        )

        prediction = model.predict(
            df
        )

        prediction_result = (
            "anomaly"
            if prediction[0] == -1
            else "normal"
        )

        conn.execute(
            text(
                """
                INSERT INTO ml_predictions
                (
                    metric_id,
                    prediction
                )
                VALUES
                (
                    :metric_id,
                    :prediction
                )
                """
            ),
            {
                "metric_id": metric_id,
                "prediction": prediction_result
            }
        )

        conn.commit()

        print(
            f"Metric {metric_id} => {prediction_result}"
        )

except Exception as e:

    print(
        f"Prediction failed: {e}"
    )
```

if **name** == "**main**":

```
predict_and_save()
```
