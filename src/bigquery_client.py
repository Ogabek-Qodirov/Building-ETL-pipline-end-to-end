from google.cloud import bigquery

# # Google Cloud Project ID
# PROJECT_ID = "ornate-variety-513309-p7"

# # BigQuery client yaratamiz
# client = bigquery.Client(project=PROJECT_ID)

# print("BigQuery connection successful!")

PROJECT_ID = "ornate-variety-513309-p7"

client = bigquery.Client(project=PROJECT_ID)

# SQL query
query = f"""
    SELECT
        Country,
        ROUND(SUM(TotalPrice), 2) AS total_revenue
    FROM `{PROJECT_ID}.retail_dataset.online_retail`
    GROUP BY Country
    ORDER BY total_revenue DESC
    LIMIT 10
"""

# Query bajariladi
query_job = client.query(query)

# Natija Pandas DataFrame'ga o'tkaziladi
df = query_job.to_dataframe()

# Natijani ekranga chiqaramiz
print(df)

# Natijani CSV faylga saqlash
df.to_csv(
    "data/processed/top_countries.csv",
    index=False
)

print("Data exported successfully!")