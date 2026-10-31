
# End-to-End ETL Pipeline with Python and BigQuery

## Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline
using the UCI Online Retail dataset.

The pipeline extracts raw retail transaction data, cleans and
transforms it using Pandas, validates data quality, and stores
the processed data in CSV and Parquet formats.

The project also explores loading and analyzing data using
Google BigQuery.

## Architecture

Extract → Transform → Validate → Load

## Technologies

- Python
- Pandas
- NumPy
- PostgreSQL / SQL
- Google BigQuery
- Parquet
- PyArrow
- Git and GitHub

## Dataset

Source: UCI Machine Learning Repository

Dataset: Online Retail

https://archive.ics.uci.edu/dataset/352/online+retail

## Project Structure

```text
01-etl-open-data/
├── data/
├── src/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

## Key Features

- Extracts retail transaction data from CSV.
- Removes duplicate records.
- Handles missing values.
- Converts columns to appropriate data types.
- Removes invalid transactions.
- Calculates total transaction value.
- Validates data quality.
- Exports processed data to CSV and Parquet.
- Tracks pipeline execution using logging.

## Data Processing Results

- Original records: 541,909
- Cleaned records: 524,878
- Removed records: 17,031
- Output formats: CSV and Parquet

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd 01-etl-open-data
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add the dataset

Download OnlineRetail.csv from the UCI dataset page
and place it inside:

```text
data/raw/
```

### 6. Run the pipeline

```bash
python main.py
```

## Author

Og'abek Qodirov

GitHub: https://github.com/Ogabek-Qodirov
