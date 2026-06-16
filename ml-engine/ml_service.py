import time

from predict_and_save import predict_and_save


def run():

    while True:

        print("Running ML prediction...")

        try:

            predict_and_save()

        except Exception as e:

            print(
                f"ML Service Error: {e}"
            )

        time.sleep(30)


if __name__ == "__main__":

    run()