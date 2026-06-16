from sqlalchemy import create_engine
from sqlalchemy import text

from rules import evaluate_rules

from actions import run_playbook

from db import (
    action_already_executed,
    save_action
)


DATABASE_URL = (
    "postgresql://admin:admin123@localhost:5432/smart_infra"
)

engine = create_engine(DATABASE_URL)


def get_latest_metric():

    with engine.connect() as conn:

        result = conn.execute(
            text(
                """
                SELECT
                    id,
                    cpu,
                    ram,
                    disk
                FROM metrics
                ORDER BY id DESC
                LIMIT 1
                """
            )
        )

        return result.fetchone()


def process_latest_metric():

    metric = get_latest_metric()

    if not metric:

        print(
            "No metrics found"
        )

        return

    print(
        f"Metric #{metric.id}"
    )

    print(
        f"CPU={metric.cpu} "
        f"RAM={metric.ram} "
        f"DISK={metric.disk}"
    )

    playbooks = evaluate_rules(
    cpu=metric.cpu,
    ram=metric.ram,
    disk=metric.disk
    )

    if not playbooks:

        print(
            "No automation actions required"
        )

        return

    for playbook in playbooks:

        if action_already_executed(
            metric.id,
            playbook
        ):

            print(
                f"Action already executed: {playbook}"
            )

            continue

        print(
            f"Running {playbook}"
        )

        success = run_playbook(
            playbook
        )

        if success:

            save_action(
                metric.id,
                playbook
            )

            print(
                f"Action logged: {playbook}"
            )


if __name__ == "__main__":

    process_latest_metric()