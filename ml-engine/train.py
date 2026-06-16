import os
import pandas as pd
import joblib

from sqlalchemy import create_engine
from sklearn.ensemble import IsolationForest

DATABASE_URL = os.getenv(
"DATABASE_URL",
"postgresql://admin:admin123@postgres:5432/smart_infra"
)

engine = create_engine(DATABASE_URL)

def load_metrics():

```
query = """
SELECT cpu, ram, disk
FROM metrics
"""

return pd.read_sql(query, engine)
```

def train():

```
try:

    df = load_metrics()

    if df.empty:

        print("No metrics found")
        return

    if len(df) < 50:

        print(
            f"Not enough data for training ({len(df)} rows found)"
        )
        return

    print(
        f"Loaded {len(df)} rows"
    )

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    model.fit(df)

    joblib.dump(
        model,
        "model/isolation_forest.pkl"
    )

    print(
        "Model saved successfully"
    )

except Exception as e:

    print(
        f"Training failed: {e}"
    )
```

if **name** == "**main**":

```
train()
```
