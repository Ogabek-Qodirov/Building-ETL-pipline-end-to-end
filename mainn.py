
from src.transform import transform_data
from src.storage import save_as_Parquet
import os
import pandas as pd

# Raw dataset
input_path = "data/raw/OnlineRetail.csv"

# Clean CSV dataset
csv_output = "data/processed/online_retail_clean.csv"

# Clean Parquet dataset
parquet_output = "data/processed/online_retail_clean.parquet"


# Step 1: Transform raw data
df = transform_data(input_path, csv_output)


# Step 2: Save as Parquet
save_as_Parquet(df, parquet_output)


# Step 3: Preview
print("\n--- FINAL DATA PREVIEW ---")
print(df.head())

print("\nDataset shape:", df.shape)

csv_size = os.path.getsize(csv_output)
parquet_size = os.path.getsize(parquet_output)

print("\n--- STORAGE COMPARISON ---")

print("CSV size:", round(csv_size / 1024 / 1024, 2), "MB")

print(
    "Parquet size:",
    round(parquet_size / 1024 / 1024, 2),
    "MB"
)

print(
    "Compression ratio:",
    round(csv_size / parquet_size, 2)
)


# Read Parquet file
parquet_df = pd.read_parquet(parquet_output)

# Check dataset dimensions
print("CSV shape:", df.shape)
print("Parquet shape:", parquet_df.shape)

# Check columns
print("\nColumns:")
print(parquet_df.columns.tolist())

# Check data types
print("\nData types:")
print(parquet_df.dtypes)

# Check total sales
print("\nCSV total sales:", df["TotalPrice"].sum())

print(
    "Parquet total sales:",
    parquet_df["TotalPrice"].sum()
)

# Verify row count
assert len(df) == len(parquet_df)

# Verify total sales
assert abs(
    df["TotalPrice"].sum()
    - parquet_df["TotalPrice"].sum()
) < 0.000001

print("\nParquet validation successful!")
