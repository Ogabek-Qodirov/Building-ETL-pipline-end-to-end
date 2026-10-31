
import logging
from pathlib import Path
import time

from src.extract import extract_data
from src.transform import transform_data
from src.storage import save_as_Parquet
from src.validation import validate_data


# Logs papkasini yaratamiz
Path("logs").mkdir(exist_ok=True)


# Logging sozlamalari
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():

    start_time = time.time()

    try:
        logging.info("ETL Pipeline started")

        # 1. Extract
        extract_start = time.time()

        df = extract_data("data/raw/OnlineRetail.csv")

        extract_time = time.time() - extract_start
        logging.info(f"Extract completed in {extract_time:.2f} seconds")

        # 2. Transform
        transform_start = time.time()

        clean_df = transform_data(
            df,
            output_path="data/processed/cleaned_data.csv"
        )

        transform_time = time.time() - transform_start
        logging.info(f"Transform completed in {transform_time:.2f} seconds")

        # 3. Load
        load_start = time.time()

        save_as_Parquet(
            clean_df,
            outputpath="data/processed/online_retail.parquet"
        )

        load_time = time.time() - load_start
        logging.info(f"Load completed in {load_time:.2f} seconds")

        # Yakuniy natijalar
        total_time = time.time() - start_time

        logging.info(f"Processed rows: {len(clean_df)}")
        logging.info(f"Total execution time: {total_time:.2f} seconds")
        logging.info("ETL Pipeline completed successfully")

        #3. Data quality Validation 
        validate_data(clean_df)
        logging.info("Data validation successful")

    except Exception:
        logging.exception("ETL Pipeline failed")
        raise



if __name__ == "__main__":
    run_pipeline()


