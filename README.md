# Week 2 – Data Collection, Cleaning and Preprocessing for Logistics Analysis

## 📌 Project Overview

This project focuses on data collection simulation, data cleaning, and preprocessing of logistics data using Python. The objective is to prepare raw logistics data for further analysis by identifying and resolving common data-quality issues.

Python and the Pandas library are used to perform the preprocessing operations.

---

## 🎯 Objectives

The main objectives of this project are:

* To simulate the collection of logistics data.
* To inspect the structure and quality of raw data.
* To identify and handle missing values.
* To remove duplicate records.
* To detect and handle potential outliers.
* To normalize numerical variables.
* To create a clean dataset suitable for further analysis.
* To understand the importance of data quality in logistics decision-making.

---

## 📊 Dataset

The project uses a simulated logistics dataset based on the characteristics of the **DataCo SMART Supply Chain for Big Data Analysis** dataset.

The reference dataset is publicly available on Kaggle:

https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis

The simulated dataset contains logistics-related fields such as:

* Shipment ID
* Shipping Mode
* Shipping Days
* Scheduled Shipping Days
* Order Quantity
* Shipping Cost
* Profit Per Order
* Delivery Status
* Customer City

The simulated dataset contains missing values and unusual observations so that different data-cleaning techniques can be demonstrated.

---

## 🧹 Data Preprocessing Steps

### 1. Data Inspection

The dataset is inspected using Pandas functions such as:

```python
df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
```

These functions help identify the structure, data types, missing values, duplicate records, and statistical characteristics of the dataset.

### 2. Duplicate Removal

Duplicate records are identified and removed using:

```python
df = df.drop_duplicates()
```

This prevents the same shipment from being counted multiple times.

### 3. Missing Value Handling

Missing numerical values are replaced using the median:

```python
df[column] = df[column].fillna(df[column].median())
```

For categorical variables, the mode is used when required.

### 4. Outlier Detection

Potential outliers are identified using the Interquartile Range (IQR) method.

The IQR is calculated as:

```text
IQR = Q3 - Q1
```

Values outside the range:

```text
Q1 - 1.5 × IQR
Q3 + 1.5 × IQR
```

are considered potential outliers.

Extreme values are capped instead of automatically deleting the complete record.

### 5. Normalization

Min-Max normalization is applied to selected numerical variables.

The formula used is:

```text
Normalized Value = (X - Xmin) / (Xmax - Xmin)
```

This converts the values to a comparable scale, generally between 0 and 1.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **CSV**
* **GitHub**

---

## 📁 Project Files

```text
Week-2/
│
├── preprocessing_pipeline.py
├── simulated_logistics_raw.csv
├── simulated_logistics_cleaned.csv
├── Week_2_Logistics_Data_Preprocessing_Report.docx
└── README.md
```

### `preprocessing_pipeline.py`

Contains the complete Python preprocessing pipeline.

### `simulated_logistics_raw.csv`

Contains the raw simulated logistics data before preprocessing.

### `simulated_logistics_cleaned.csv`

Contains the dataset after missing-value handling, duplicate removal, outlier treatment, and normalization.

### `Week_2_Logistics_Data_Preprocessing_Report.docx`

Contains the detailed methodology, explanations, Python code, reflection, and conclusion for the internship task.

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install Required Libraries

Open Command Prompt or Terminal and run:

```bash
pip install pandas numpy
```

### Step 3: Run the Python File

Keep the Python file and raw CSV file in the same folder.

Then run:

```bash
python preprocessing_pipeline.py
```

### Step 4: Check the Output

After successful execution, the program creates:

```text
simulated_logistics_cleaned.csv
```

This file contains the cleaned and normalized data.

---

## 📈 Expected Outcome

After preprocessing:

* Duplicate records are removed.
* Missing numerical values are handled using median values.
* Missing categorical values are handled using the mode when required.
* Potential outliers are identified using the IQR method.
* Extreme values are capped.
* Selected numerical variables are normalized.
* A cleaned CSV file is generated for further analysis.

---

## 💡 Learning Outcome

Through this project, I learned how raw logistics data can be transformed into a structured and analysis-ready dataset. I gained practical experience with Pandas functions for inspecting, cleaning, transforming, and exporting data.

The project also helped me understand the importance of handling missing values and outliers carefully because poor-quality data can affect logistics metrics and lead to inaccurate business decisions.

---

## 🔮 Future Scope

The cleaned dataset can be used for further logistics analysis, including:

* Delivery performance analysis
* Shipping cost analysis
* Late-delivery analysis
* Exploratory Data Analysis (EDA)
* Data visualization
* Logistics KPI calculation
* Predictive analytics
* Machine-learning models for delivery prediction

---

## 👩‍💻 Author

**Name:** Sharanya
**Course:** BCA
**Internship:** [logistics data analyst internship]
**Task:** Week 2 – Data Collection, Cleaning and Preprocessing
