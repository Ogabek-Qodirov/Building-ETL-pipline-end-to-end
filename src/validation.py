
import logging


def validate_data(df):

    logging.info("Data quality validation started")

    # 1. DataFrame bo'sh emasligini tekshiramiz
    if df.empty:
        raise ValueError("DataFrame is empty!")

    # 2. Muhim ustunlarda NULL qiymatlarni tekshiramiz
    required_columns = [
        "InvoiceNo",
        "StockCode",
        "InvoiceDate",
        "Quantity",
        "UnitPrice"
    ]

    for column in required_columns:

        if df[column].isnull().any():
            raise ValueError(f"NULL values found in {column}")

    # 3. Quantity musbatligini tekshiramiz
    if (df["Quantity"] <= 0).any():
        raise ValueError("Invalid Quantity values found!")

    # 4. UnitPrice musbatligini tekshiramiz
    if (df["UnitPrice"] <= 0).any():
        raise ValueError("Invalid UnitPrice values found!")

    # 5. Duplicate qatorlarni tekshiramiz
    if df.duplicated().any():
        raise ValueError("Duplicate rows found!")

    logging.info("All data quality checks passed")

    return True
