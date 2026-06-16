import time

from collector import collect_metrics
from sender import send_metrics


def main():

    while True:

        metrics = collect_metrics()

        print("Collected Metrics:")
        print(metrics)

        result = send_metrics(metrics)

        print("Server Response:")
        print(result)

        print("Waiting 30 seconds...\n")

        time.sleep(30)


if __name__ == "__main__":
    main()