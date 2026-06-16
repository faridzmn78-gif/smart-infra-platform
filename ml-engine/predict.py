import joblib
import pandas as pd


model = joblib.load(
    "model/isolation_forest.pkl"
)


def predict_metric(
    cpu,
    ram,
    disk
):

    df = pd.DataFrame(
        [
            {
                "cpu": cpu,
                "ram": ram,
                "disk": disk
            }
        ]
    )

    prediction = model.predict(df)

    if prediction[0] == -1:
        return "anomaly"

    return "normal"


if __name__ == "__main__":

    print(
        predict_metric(
            cpu=95,
            ram=90,
            disk=95
        )
    )