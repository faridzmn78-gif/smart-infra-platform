def evaluate_rules(
    cpu,
    ram,
    disk
):

    actions = []

    if cpu >= 90:

        actions.append(
            "restart_docker.yml"
        )

    if ram >= 90:

        actions.append(
            "restart_apache.yml"
        )

    if disk >= 95:

        actions.append(
            "cleanup_disk.yml"
        )

    return actions