# from ucimlrepo import fetch_ucirepo

# # Download dataset from UCI
# dataset = fetch_ucirepo(id=352)

# # Get features
# df = dataset.data.features

# # Save as Excel
# df.to_excel("data/raw/Online Retail.xlsx", index=False)

# print("Dataset downloaded successfully!")
# print(df.shape)



# import pandas as pd

# # 1. Dataset file path
# file_path = "data/raw/OnlineRetail.csv"

# # 2. Read CSV file
# df = pd.read_csv(file_path, encoding="ISO-8859-1")

# # 3. Display first 5 rows
# print(df.head())

# # 4. Display dataset dimensions
# print("Dataset shape:", df.shape)

# #Information about the Data 
# df.info()

# #Satatistic info 
# print(df.describe())

#infromation about Quantity information
#print(df['Quantity'].describe())


#Prints all the amount of the missing values 
# print(df.isnull().sum())

#We can print all the missing values by precentage of them     
# missing_percent = (
#      df.isnull().sum() / len(df)
#  ) * 100

# print(missing_percent)

#Duplicate values 
#print("Duplicate rows:", df.duplicated().sum())

# duplicates = df[df.duplicated()]
# print(duplicates.head())



import pandas as pd

# ==================================
# 1. LOAD DATASET
# ==================================

file_path = "data/raw/OnlineRetail.csv"

df = pd.read_csv(file_path, encoding="ISO-8859-1")


# ==================================
# 2. BASIC INFORMATION
# ==================================

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- LAST 5 ROWS ---")
print(df.tail())


# ==================================
# 3. DATA INFORMATION
# ==================================

print("\n--- DATA INFO ---")
df.info()


# ==================================
# 4. STATISTICAL ANALYSIS
# ==================================

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())

print("\n--- CATEGORICAL STATISTICS ---")
print(df.describe(include="object"))


# ==================================
# 5. MISSING VALUES
# ==================================

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- MISSING VALUES PERCENTAGE ---")
print((df.isnull().sum() / len(df)) * 100)


# ==================================
# 6. DUPLICATE VALUES
# ==================================

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())


# ==================================
# 7. DATA TYPES
# ==================================

print("\n--- DATA TYPES ---")
print(df.dtypes)
