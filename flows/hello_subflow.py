from prefect import task, flow
from prefect import get_run_logger
from flows.healthcheck import healthcheck


@task
def say_hi(user_name: str):
    logger = get_run_logger()
    logger.info("Hello from Prefect and GitHub Actions, %s! 👋", user_name)


@flow
def hello_subflow(user: str = "Marvin"):
    say_hi(user)
    healthcheck()


if __name__ == "__main__":
    hello_subflow(user="Anna")
