# Logistics Data Analyst Internship - Week 1
# Strategic Planning and Data Exploration

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "logistics_shipments.csv"

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    print("Dataset shape:", df.shape)
    print("Missing values:\n", df.isnull().sum())

    df = df.drop_duplicates()

    for col in ["dispatch_date", "delivery_date", "promised_date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    if {"dispatch_date", "delivery_date"}.issubset(df.columns):
        df["delivery_days"] = (
            df["delivery_date"] - df["dispatch_date"]
        ).dt.days

    if {"delivery_date", "promised_date"}.issubset(df.columns):
        df["is_late"] = (
            df["delivery_date"] > df["promised_date"]
        ).astype(int)

    return df

def calculate_kpis(df):
    kpis = {}

    if "is_late" in df.columns:
        kpis["On-time delivery rate (%)"] = (1 - df["is_late"].mean()) * 100
        kpis["Delay rate (%)"] = df["is_late"].mean() * 100

    if "delivery_days" in df.columns:
        kpis["Average delivery time (days)"] = df["delivery_days"].mean()

    if "shipping_cost" in df.columns:
        kpis["Average shipping cost"] = df["shipping_cost"].mean()

    if {"shipping_cost", "distance_km"}.issubset(df.columns):
        valid = df["distance_km"] > 0
        kpis["Average cost per km"] = (
            df.loc[valid, "shipping_cost"] / df.loc[valid, "distance_km"]
        ).mean()

    return kpis

def explore_data(df):
    print("\nDescriptive statistics:")
    print(df.describe(include="all"))

    if "shipping_mode" in df.columns and "delivery_days" in df.columns:
        print("\nAverage delivery time by shipping mode:")
        print(df.groupby("shipping_mode")["delivery_days"].mean())

    if "delivery_days" in df.columns:
        df["delivery_days"].dropna().plot(
            kind="hist", bins=20, title="Distribution of Delivery Time"
        )
        plt.xlabel("Delivery Time (days)")
        plt.ylabel("Number of Shipments")
        plt.tight_layout()
        plt.show()

def main():
    try:
        df = load_and_clean_data(DATA_FILE)
    except FileNotFoundError:
        print("Dataset not found. Place the selected dataset in this folder "
              "and name it 'logistics_shipments.csv'.")
        return

    print("\nKey Performance Indicators:")
    for name, value in calculate_kpis(df).items():
        if pd.notna(value):
            print(f"{name}: {value:.2f}")

    explore_data(df)

if __name__ == "__main__":
    main()
