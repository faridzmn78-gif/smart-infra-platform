from sqlalchemy import create_engine
from sqlalchemy import text
import os

DATABASE_URL = os.getenv(
"DATABASE_URL",
"postgresql://admin:admin123@localhost:5432/smart_infra"
)

engine = create_engine(DATABASE_URL)

def action_already_executed(
metric_id,
action
):

```
with engine.connect() as conn:

    result = conn.execute(
        text(
            """
            SELECT id
            FROM automation_logs
            WHERE metric_id = :metric_id
            AND action = :action
            LIMIT 1
            """
        ),
        {
            "metric_id": metric_id,
            "action": action
        }
    )

    return result.fetchone() is not None
```

def save_action(
metric_id,
action
):

```
with engine.connect() as conn:

    conn.execute(
        text(
            """
            INSERT INTO automation_logs
            (
                metric_id,
                action
            )
            VALUES
            (
                :metric_id,
                :action
            )
            """
        ),
        {
            "metric_id": metric_id,
            "action": action
        }
    )

    conn.commit()
```
