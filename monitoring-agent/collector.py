import psutil
import platform
import socket


def collect_metrics():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    hostname = socket.gethostname()

    operating_system = platform.system()

    os_version = platform.release()

    return {
        "hostname": hostname,
        "os": operating_system,
        "os_version": os_version,
        "cpu": cpu,
        "ram": ram,
        "disk": disk
    }


if __name__ == "__main__":

    metrics = collect_metrics()

    print("System Metrics:")

    print(metrics)