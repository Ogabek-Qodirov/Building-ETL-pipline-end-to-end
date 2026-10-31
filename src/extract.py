
import pandas as pd
import logging
from pathlib import Path


def extract_data(file_path):

    try:
        # Fayl mavjudligini tekshiramiz
        if not Path(file_path).exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        logging.info("Starting data extraction")

        # CSV faylni o'qiymiz
        df = pd.read_csv(
            file_path,
            encoding="ISO-8859-1",
            dtype={
                "InvoiceNo": "str",
                "StockCode": "str"
            }
        )

        logging.info(
            f"Extraction successful: {len(df)} rows"
        )

        return df

    except FileNotFoundError:
        logging.exception("CSV file does not exist")
        raise

    except pd.errors.ParserError:
        logging.exception("CSV parsing failed")
        raise

    except Exception:
        logging.exception("Unexpected extraction error")
        raise
