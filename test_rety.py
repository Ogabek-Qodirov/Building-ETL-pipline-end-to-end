
import logging
from src.retry import retry_operation

logging.basicConfig(level=logging.INFO)

attempts = 0


def unstable_operation():

    global attempts

    attempts += 1

    print(f"Running attempt: {attempts}")

    if attempts < 3:
        raise ConnectionError("Temporary connection error")

    return "Data loaded successfully!"


result = retry_operation(
    unstable_operation,
    max_attempts=3
)

print(result)
