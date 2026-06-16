import requests


def send_metrics(metrics):

    url = "http://backend:8000/metrics"

    response = requests.post(
        url,
        json=metrics
    )

    return response.json()