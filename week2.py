import pandas as pd
import numpy as np

# ---------------------------------------------------------
# WEEK 2: DATA CLEANING AND PREPROCESSING
# Logistics Analysis
# ---------------------------------------------------------

# 1. Load the raw logistics dataset
df = pd.read_csv("simulated_logistics_raw.csv")

print("Original Dataset:")
print(df.head())

# ---------------------------------------------------------
# 2. Check the dataset
# ---------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nNumber of Duplicate Records:")
print(df.duplicated().sum())

# Display basic statistics
print("\nStatistical Summary:")
print(df.describe())


# ---------------------------------------------------------
# 3. Remove Duplicate Records
# ---------------------------------------------------------

df = df.drop_duplicates()

print("\nDuplicates after cleaning:")
print(df.duplicated().sum())


# ---------------------------------------------------------
# 4. Handle Missing Numerical Values
# ---------------------------------------------------------

numeric_columns = [
    "Shipping_Days",
    "Shipping_Cost",
    "Order_Quantity",
    "Profit_Per_Order"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())


# ---------------------------------------------------------
# 5. Handle Missing Categorical Values
# ---------------------------------------------------------

categorical_columns = [
    "Shipping_Mode",
    "Delivery_Status",
    "Customer_City"
]

for column in categorical_columns:

    if df[column].isnull().any():
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )


# ---------------------------------------------------------
# 6. Outlier Detection using IQR
# ---------------------------------------------------------

def cap_outliers_iqr(data, column):

    # Calculate first quartile
    Q1 = data[column].quantile(0.25)

    # Calculate third quartile
    Q3 = data[column].quantile(0.75)

    # Calculate IQR
    IQR = Q3 - Q1

    # Calculate lower and upper limits
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    # Count outliers
    outliers = (
        (data[column] < lower_limit) |
        (data[column] > upper_limit)
    ).sum()

    print(
        f"{column}: {outliers} potential outlier(s)"
    )

    # Cap extreme values
    data[column] = data[column].clip(
        lower=lower_limit,
        upper=upper_limit
    )

    return data


# Apply IQR method
outlier_columns = [
    "Shipping_Days",
    "Order_Quantity",
    "Shipping_Cost"
]

print("\nOutlier Detection:")

for column in outlier_columns:
    df = cap_outliers_iqr(df, column)


# ---------------------------------------------------------
# 7. Min-Max Normalization
# ---------------------------------------------------------

def min_max_normalization(series):

    return (
        (series - series.min()) /
        (series.max() - series.min())
    )


normalization_columns = [
    "Shipping_Days",
    "Order_Quantity",
    "Shipping_Cost"
]

for column in normalization_columns:

    df[column + "_Normalized"] = (
        min_max_normalization(df[column])
    )


# ---------------------------------------------------------
# 8. Final Data Quality Check
# ---------------------------------------------------------

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset:")
print(df.head())


# ---------------------------------------------------------
# 9. Save the Cleaned Dataset
# ---------------------------------------------------------

df.to_csv(
    "simulated_logistics_cleaned.csv",
    index=False
)

print(
    "\nCleaned dataset saved successfully!"
)
