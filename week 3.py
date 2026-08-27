import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# WEEK 3
# ADVANCED DATA ANALYSIS AND VISUALIZATION IN LOGISTICS
# ---------------------------------------------------------

# Set random seed so the results remain reproducible
np.random.seed(42)

# ---------------------------------------------------------
# 1. CREATE HYPOTHETICAL LOGISTICS DATASET
# ---------------------------------------------------------

n = 100

months = np.random.choice(
    ["January", "February", "March", "April",
     "May", "June"],
    n
)

regions = np.random.choice(
    ["North", "South", "East", "West"],
    n
)

transport_modes = np.random.choice(
    ["Road", "Rail", "Air", "Sea"],
    n
)

shipment_volume = np.random.randint(
    20, 500, n
)

distance = np.random.randint(
    50, 1500, n
)

delivery_time = np.round(
    2 + (distance / 500) +
    np.random.normal(0, 1, n),
    1
)

# Make sure delivery time does not become negative
delivery_time = np.maximum(
    delivery_time,
    1
)

transportation_cost = np.round(
    500 +
    (distance * 2.5) +
    (shipment_volume * 3) +
    np.random.normal(0, 500, n),
    2
)

transportation_cost = np.maximum(
    transportation_cost,
    100
)

delivery_status = np.where(
    delivery_time <= 5,
    "On Time",
    "Late"
)

# Create DataFrame
df = pd.DataFrame({
    "Shipment_ID": range(1001, 1001 + n),
    "Month": months,
    "Region": regions,
    "Transport_Mode": transport_modes,
    "Shipment_Volume": shipment_volume,
    "Delivery_Time": delivery_time,
    "Transportation_Cost": transportation_cost,
    "Distance": distance,
    "Delivery_Status": delivery_status
})


# ---------------------------------------------------------
# 2. SAVE DATASET
# ---------------------------------------------------------

df.to_csv(
    "logistics_analysis_data.csv",
    index=False
)

print("Dataset created successfully.")


# ---------------------------------------------------------
# 3. BASIC DATA EXPLORATION
# ---------------------------------------------------------

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ---------------------------------------------------------
# 4. CENTRAL TENDENCY
# ---------------------------------------------------------

print("\nAverage Delivery Time:",
      round(df["Delivery_Time"].mean(), 2))

print("Median Delivery Time:",
      round(df["Delivery_Time"].median(), 2))

print("\nAverage Transportation Cost:",
      round(
          df["Transportation_Cost"].mean(),
          2
      ))

print("Median Transportation Cost:",
      round(
          df["Transportation_Cost"].median(),
          2
      ))


# ---------------------------------------------------------
# 5. HISTOGRAM - DELIVERY TIME
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Delivery_Time"],
    bins=10
)

plt.title(
    "Distribution of Delivery Time"
)

plt.xlabel(
    "Delivery Time (Days)"
)

plt.ylabel(
    "Number of Shipments"
)

plt.tight_layout()

plt.savefig(
    "delivery_time_distribution.png"
)

plt.show()


# ---------------------------------------------------------
# 6. BAR CHART - TRANSPORTATION COST
# ---------------------------------------------------------

mode_cost = df.groupby(
    "Transport_Mode"
)["Transportation_Cost"].mean()

plt.figure(figsize=(8, 5))

mode_cost.plot(
    kind="bar"
)

plt.title(
    "Average Transportation Cost by Mode"
)

plt.xlabel(
    "Transport Mode"
)

plt.ylabel(
    "Average Transportation Cost"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "transportation_cost_by_mode.png"
)

plt.show()


# ---------------------------------------------------------
# 7. MONTHLY SHIPMENT VOLUME
# ---------------------------------------------------------

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June"
]

monthly_volume = (
    df.groupby("Month")["Shipment_Volume"]
    .sum()
    .reindex(month_order)
)

plt.figure(figsize=(9, 5))

plt.plot(
    monthly_volume.index,
    monthly_volume.values,
    marker="o"
)

plt.title(
    "Monthly Shipment Volume"
)

plt.xlabel(
    "Month"
)

plt.ylabel(
    "Total Shipment Volume"
)

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "monthly_shipment_volume.png"
)

plt.show()


# ---------------------------------------------------------
# 8. SCATTER PLOT - DISTANCE VS DELIVERY TIME
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Distance",
    y="Delivery_Time"
)

plt.title(
    "Distance vs Delivery Time"
)

plt.xlabel(
    "Distance (km)"
)

plt.ylabel(
    "Delivery Time (Days)"
)

plt.tight_layout()

plt.savefig(
    "distance_vs_delivery_time.png"
)

plt.show()


# ---------------------------------------------------------
# 9. DELIVERY STATUS
# ---------------------------------------------------------

status_count = (
    df["Delivery_Status"]
    .value_counts()
)

plt.figure(figsize=(7, 5))

status_count.plot(
    kind="bar"
)

plt.title(
    "Delivery Status Distribution"
)

plt.xlabel(
    "Delivery Status"
)

plt.ylabel(
    "Number of Shipments"
)

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "delivery_status.png"
)

plt.show()


# ---------------------------------------------------------
# 10. BOX PLOT - TRANSPORTATION COST
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    x=df["Transportation_Cost"]
)

plt.title(
    "Transportation Cost Distribution"
)

plt.xlabel(
    "Transportation Cost"
)

plt.tight_layout()

plt.savefig(
    "transportation_cost_boxplot.png"
)

plt.show()


# ---------------------------------------------------------
# 11. CORRELATION ANALYSIS
# ---------------------------------------------------------

numeric_columns = [
    "Shipment_Volume",
    "Delivery_Time",
    "Transportation_Cost",
    "Distance"
]

correlation = df[
    numeric_columns
].corr()

print("\nCorrelation Matrix:")
print(correlation)


# ---------------------------------------------------------
# 12. CORRELATION HEATMAP
# ---------------------------------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f"
)

plt.title(
    "Correlation Between Logistics Variables"
)

plt.tight_layout()

plt.savefig(
    "logistics_correlation_heatmap.png"
)

plt.show()


# ---------------------------------------------------------
# 13. FINAL MESSAGE
# ---------------------------------------------------------

print("\nAnalysis and visualization completed successfully!")

print("\nGenerated Files:")
print("1. logistics_analysis_data.csv")
print("2. delivery_time_distribution.png")
print("3. transportation_cost_by_mode.png")
print("4. monthly_shipment_volume.png")
print("5. distance_vs_delivery_time.png")
print("6. delivery_status.png")
print("7. transportation_cost_boxplot.png")
print("8. logistics_correlation_heatmap.png")
