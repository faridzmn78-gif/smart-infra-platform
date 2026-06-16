from rules import (
    evaluate_rules
)

from actions import (
    run_playbook
)


def process_metric(
    cpu,
    ram,
    disk
):

    playbooks = evaluate_rules(
        cpu,
        ram,
        disk
    )

    if not playbooks:

        print(
            "No automation actions required"
        )

        return

    for playbook in playbooks:

        print(
            f"Running {playbook}"
        )

        run_playbook(
            playbook
        )


if __name__ == "__main__":

    process_metric(
        cpu=95,
        ram=20,
        disk=10
    )