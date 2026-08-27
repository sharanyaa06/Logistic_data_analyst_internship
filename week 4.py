import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import cross_val_score


# =========================================================
# WEEK 4
# PREDICTIVE MODELING AND OPTIMIZATION IN LOGISTICS
# =========================================================


# ---------------------------------------------------------
# 1. CREATE HYPOTHETICAL LOGISTICS DATASET
# ---------------------------------------------------------

np.random.seed(42)

n = 150

shipment_volume = np.random.randint(
    20, 500, n
)

distance = np.random.randint(
    50, 1500, n
)

transport_modes = np.random.choice(
    ["Road", "Rail", "Air", "Sea"],
    n
)

# Create transportation cost
transportation_cost = (
    500
    + distance * 2.5
    + shipment_volume * 3
    + np.random.normal(0, 400, n)
)

transportation_cost = np.maximum(
    transportation_cost,
    100
)

# Create delivery time
delivery_time = (
    1.5
    + distance / 450
    + shipment_volume / 1000
    + np.random.normal(0, 0.8, n)
)

delivery_time = np.maximum(
    delivery_time,
    1
)

# Create DataFrame
df = pd.DataFrame({
    "Shipment_ID": range(1001, 1001 + n),
    "Shipment_Volume": shipment_volume,
    "Distance": distance,
    "Transportation_Cost":
        np.round(
            transportation_cost,
            2
        ),
    "Transport_Mode": transport_modes,
    "Delivery_Time":
        np.round(
            delivery_time,
            2
        )
})


# ---------------------------------------------------------
# 2. SAVE DATASET
# ---------------------------------------------------------

df.to_csv(
    "logistics_prediction_data.csv",
    index=False
)

print("Dataset created successfully.")

print("\nFirst Five Records:")
print(df.head())


# ---------------------------------------------------------
# 3. DATA INSPECTION
# ---------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())


# ---------------------------------------------------------
# 4. ENCODE TRANSPORT MODE
# ---------------------------------------------------------

df = pd.get_dummies(
    df,
    columns=["Transport_Mode"],
    drop_first=True
)


# ---------------------------------------------------------
# 5. DEFINE FEATURES AND TARGET
# ---------------------------------------------------------

X = df.drop(
    ["Shipment_ID", "Delivery_Time"],
    axis=1
)

y = df["Delivery_Time"]


# ---------------------------------------------------------
# 6. TRAIN-TEST SPLIT
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Records:",
      len(X_train))

print("Testing Records:",
      len(X_test))


# ---------------------------------------------------------
# 7. LINEAR REGRESSION
# ---------------------------------------------------------

linear_model = LinearRegression()

linear_model.fit(
    X_train,
    y_train
)

linear_predictions = (
    linear_model.predict(X_test)
)


# ---------------------------------------------------------
# 8. DECISION TREE REGRESSION
# ---------------------------------------------------------

tree_model = DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

tree_model.fit(
    X_train,
    y_train
)

tree_predictions = (
    tree_model.predict(X_test)
)


# ---------------------------------------------------------
# 9. MODEL EVALUATION FUNCTION
# ---------------------------------------------------------

def evaluate_model(
    actual,
    predicted,
    model_name
):

    mae = mean_absolute_error(
        actual,
        predicted
    )

    rmse = np.sqrt(
        mean_squared_error(
            actual,
            predicted
        )
    )

    r2 = r2_score(
        actual,
        predicted
    )

    print("\n" + model_name)

    print("MAE:",
          round(mae, 3))

    print("RMSE:",
          round(rmse, 3))

    print("R2:",
          round(r2, 3))

    return mae, rmse, r2


# ---------------------------------------------------------
# 10. EVALUATE BOTH MODELS
# ---------------------------------------------------------

linear_results = evaluate_model(
    y_test,
    linear_predictions,
    "Linear Regression"
)

tree_results = evaluate_model(
    y_test,
    tree_predictions,
    "Decision Tree Regression"
)


# ---------------------------------------------------------
# 11. MODEL COMPARISON
# ---------------------------------------------------------

comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree"
    ],

    "MAE": [
        linear_results[0],
        tree_results[0]
    ],

    "RMSE": [
        linear_results[1],
        tree_results[1]
    ],

    "R2": [
        linear_results[2],
        tree_results[2]
    ]
})

print("\nModel Comparison:")
print(comparison)


# ---------------------------------------------------------
# 12. CROSS-VALIDATION
# ---------------------------------------------------------

cv_scores = cross_val_score(
    tree_model,
    X,
    y,
    cv=5,
    scoring="r2"
)

print("\nDecision Tree Cross-Validation R2 Scores:")
print(cv_scores)

print(
    "Average Cross-Validation R2:",
    round(cv_scores.mean(), 3)
)


# ---------------------------------------------------------
# 13. ACTUAL VS PREDICTED
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    y_test,
    tree_predictions
)

plt.xlabel(
    "Actual Delivery Time"
)

plt.ylabel(
    "Predicted Delivery Time"
)

plt.title(
    "Actual vs Predicted Delivery Time"
)

plt.tight_layout()

plt.savefig(
    "actual_vs_predicted.png"
)

plt.show()


# ---------------------------------------------------------
# 14. FEATURE IMPORTANCE
# ---------------------------------------------------------

importance = pd.Series(
    tree_model.feature_importances_,
    index=X.columns
)

importance = importance.sort_values(
    ascending=False
)

print("\nFeature Importance:")
print(importance)

plt.figure(figsize=(8, 5))

importance.plot(
    kind="bar"
)

plt.title(
    "Feature Importance for Delivery Time Prediction"
)

plt.xlabel(
    "Features"
)

plt.ylabel(
    "Importance"
)

plt.tight_layout()

plt.savefig(
    "feature_importance.png"
)

plt.show()


# ---------------------------------------------------------
# 15. MODEL ERROR COMPARISON
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    comparison["Model"],
    comparison["RMSE"]
)

plt.title(
    "Model Comparison Using RMSE"
)

plt.xlabel(
    "Model"
)

plt.ylabel(
    "RMSE"
)

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    "model_rmse_comparison.png"
)

plt.show()


# ---------------------------------------------------------
# 16. FINAL OUTPUT
# ---------------------------------------------------------

print("\n===================================")
print("PREDICTIVE ANALYSIS COMPLETED")
print("===================================")

print("\nGenerated Files:")

print("1. logistics_prediction_data.csv")
print("2. actual_vs_predicted.png")
print("3. feature_importance.png")
print("4. model_rmse_comparison.png")
