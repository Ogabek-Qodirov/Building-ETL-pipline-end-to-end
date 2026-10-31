#Goal
# Muammo	             Bizning qarorimiz
# Duplicate rows	     Takrorlangan qatorlarni olib tashlaymiz
# Missing CustomerID	 Qatorni saqlaymiz
# Missing Description  	 Unknown bilan to'ldiramiz
# Negative Quantity	     Bekor qilish operatsiyalarini alohida ko'rib chiqamiz
# UnitPrice = 0	         Savdo tahlilidan chiqaramiz
# Invalid InvoiceDate	 Yaroqsiz sanalarni chiqaramiz
# Negative UnitPrice	 Savdo tahlilidan chiqaramiz

import pandas as pd


def transform_data(df, output_path):

    print("Transforming data...")

    # Duplicate qatorlarni olib tashlaymiz
    df = df.drop_duplicates()

    # Data type larni o'zgartiramiz
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    # Muhim ustunlarda NULL bo'lgan qatorlarni olib tashlaymiz
    df = df.dropna(
        subset=[
            "InvoiceNo",
            "StockCode",
            "InvoiceDate",
            "Quantity",
            "UnitPrice"
        ]
    )

    # Description NULL qiymatlarini to'ldiramiz
    df["Description"] = df["Description"].fillna("Unknown")

    # Bekor qilingan buyurtmalarni olib tashlaymiz
    df = df[~df["InvoiceNo"].str.startswith("C")]

    # Manfiy yoki nol Quantity qiymatlarini olib tashlaymiz
    df = df[df["Quantity"] > 0]

    # Noto'g'ri narxlarni olib tashlaymiz
    df = df[df["UnitPrice"] > 0]

    # Umumiy narxni hisoblaymiz
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Indexni qayta tartiblaymiz
    df = df.reset_index(drop=True)

    # Tozalangan ma'lumotni CSV ga saqlaymiz
    df.to_csv(output_path, index=False)

    print(f"Transform completed: {len(df)} rows")

    return df