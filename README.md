# Week 4 – Predictive Modeling and Optimization in Logistics Systems

## 📌 Project Overview

This project focuses on applying predictive modeling and optimization concepts to a logistics problem using Python.

The objective is to predict shipment delivery time using logistics-related variables such as shipment volume, transportation distance, transportation cost, and transport mode.

Two machine-learning regression models are implemented:

* Linear Regression
* Decision Tree Regression

The models are evaluated using MAE, RMSE, and R² metrics.

---

## 🎯 Objectives

The main objectives of this project are:

* Define a logistics-related prediction problem.
* Generate a hypothetical logistics dataset.
* Prepare data for machine learning.
* Select relevant features and target variables.
* Train predictive regression models.
* Evaluate model performance.
* Compare different predictive models.
* Perform cross-validation.
* Identify important prediction features.
* Propose logistics optimization strategies.

---

## 📊 Prediction Problem

The prediction problem addressed in this project is:

> **Predict the delivery time of a logistics shipment using available shipment and transportation information.**

### Target Variable

`Delivery_Time`

### Input Features

* Shipment Volume
* Distance
* Transportation Cost
* Transport Mode

---

## 📁 Dataset

A hypothetical logistics dataset is generated programmatically using NumPy and Pandas.

The dataset contains 150 shipment records.

The following variables are included:

| Variable            | Description                           |
| ------------------- | ------------------------------------- |
| Shipment_ID         | Unique shipment identifier            |
| Shipment_Volume     | Number of units in shipment           |
| Distance            | Transportation distance in kilometres |
| Transportation_Cost | Transportation cost                   |
| Transport_Mode      | Road, Rail, Air, or Sea               |
| Delivery_Time       | Delivery duration in days             |

The dataset is automatically saved as:

```text
logistics_prediction_data.csv
```

when the Python script is executed.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* GitHub

---

## 🤖 Machine Learning Models

### 1. Linear Regression

Linear Regression is used as a baseline model because it is simple, efficient, and easy to interpret.

### 2. Decision Tree Regression

Decision Tree Regression is used as a comparison model because it can identify non-linear relationships between logistics variables.

---

## 📏 Evaluation Metrics

The models are evaluated using:

### MAE – Mean Absolute Error

Measures the average absolute difference between actual and predicted delivery times.

Lower values indicate better performance.

### RMSE – Root Mean Squared Error

Measures prediction error while giving greater importance to larger errors.

Lower values indicate better performance.

### R² – R-squared

Measures how much variation in delivery time is explained by the model.

A higher value generally indicates better performance.

---

## 🔄 Cross-Validation

Five-fold cross-validation is used to provide a more reliable estimate of model performance.

The dataset is divided into five sections, and each section is used as a validation set while the remaining sections are used for training.

---

## 📊 Visualizations

The Python script generates:

### Actual vs Predicted Delivery Time

Shows how closely the predicted delivery times match actual delivery times.

### Feature Importance

Shows the relative importance of the input variables in the Decision Tree model.

### Model RMSE Comparison

Compares the prediction error of Linear Regression and Decision Tree Regression.

---

## ⚙️ Optimization Strategies

The predictive insights can be used to improve logistics operations through:

* Route optimization
* Transportation mode selection
* Resource allocation
* Early identification of delayed shipments
* Transportation cost optimization
* Monitoring high-risk shipments

---

## 💡 Key Learning Outcomes

Through this project, I learned:

* How to define a machine-learning problem.
* How to create a logistics dataset.
* How to prepare data for predictive modeling.
* How to split data into training and testing sets.
* How to implement regression models.
* How to evaluate machine-learning models.
* How to perform cross-validation.
* How to interpret feature importance.
* How predictive analytics can support logistics decisions.
* How machine learning can be combined with operational optimization.

---

## 🔮 Future Scope

The project can be extended by:

* Using real logistics datasets.
* Testing Random Forest and ensemble models.
* Performing hyperparameter tuning.
* Predicting late-delivery probability.
* Forecasting shipment volumes.
* Building an interactive logistics dashboard.
* Integrating real-time logistics data.
* Implementing route optimization algorithms.

---

## ▶️ How to Run

### Install Required Libraries

```bash
pip install pandas numpy scikit-learn matplotlib
```

### Run the Python Script

```bash
python logistics_prediction_model.py
```

The script automatically generates the dataset and visualization files.

---

## 📁 Project Structure

```text
Week-4/
│
├── logistics_prediction_model.py
├── logistics_prediction_data.csv
├── actual_vs_predicted.png
├── feature_importance.png
├── model_rmse_comparison.png
├── Week_4_Predictive_Modeling_Report.docx
└── README.md
```

---

## 👩‍💻 Author

**Name:** [Sharanya]
**Course:** BCA
**Internship:** [logical data analyst]
**Task:** Week 4 – Predictive Modeling and Optimization in Logistics Systems
