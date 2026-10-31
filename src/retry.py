
import time
import logging


def retry_operation(operation, max_attempts=3):

    for attempt in range(1, max_attempts + 1):

        try:
            logging.info(
                f"Attempt {attempt}/{max_attempts}"
            )

            result = operation()

            logging.info("Operation successful")

            return result

        except Exception:

            logging.exception(
                f"Attempt {attempt} failed"
            )

            if attempt == max_attempts:
                logging.error("All retry attempts failed")
                raise

            time.sleep(2)
