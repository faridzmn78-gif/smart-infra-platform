import subprocess


def run_playbook(playbook_name):

    playbook_path = (
        f"ansible/playbooks/{playbook_name}"
    )

    inventory_path = (
        "ansible/inventory/hosts.ini"
    )

    try:

        result = subprocess.run(
            [
                "wsl",
                "ansible-playbook",
                "-i",
                inventory_path,
                playbook_path
            ],
            capture_output=True,
            text=True
        )

        print(result.stdout)

        return result.returncode == 0

    except Exception as e:

        print(
            f"Playbook execution failed: {e}"
        )

        return False