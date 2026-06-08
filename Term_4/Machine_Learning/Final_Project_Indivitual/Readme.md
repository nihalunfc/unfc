# Machine Learning Final Project: Health Risk Tier Classification

## 📌 Project Overview
This repository contains my final individual project for the Machine Learning course. The objective of this project is to build, evaluate, and analyze machine learning models to predict a patient's health risk tier based on various physiological and lifestyle factors. 

A major focus of my project will be developing an Artificial Neural Network (ANN/MLP) and comparing its performance, behavior, and generalization capabilities against classical baseline machine learning models.

## 📊 Dataset Description
**Dataset:** `Health_Risk_Tiers_v2`
The dataset is a synthetic healthcare dataset featuring non-linear relationships and multi-class target variables. 

* **Target Variable:** `risk_tier` (0 = Low Risk, 1 = Medium Risk, 2 = High Risk)
* **Features:** 10 features including numeric (Age, BMI, Blood Pressure, Glucose, Sleep Hours, Stress Level, Cholesterol), categorical (`physical_activity`), binary (`family_history`), and a non-informative identifier (`patient_id`).
* **Known Data Challenges:** Contains approximately ~8% missing values in the `cholesterol` column that will require imputation.

---

## 🗺️ Step-by-Step Execution Plan

To ensure a structured and methodical approach to this project, I will follow the pipeline outlined below. I will update this repository as I complete each phase.

### Phase 1: Exploratory Data Analysis (EDA) & Preprocessing
* **Objective:** Understand the data distribution and prepare it for modeling.
* **Tasks:**
  * Drop the non-informative `patient_id` column to prevent data leakage/noise.
  * Perform univariate and bivariate analysis to understand feature relationships with `risk_tier`.
  * **Handling Missing Data:** Analyze the ~8% missing data in the `cholesterol` column and apply an appropriate imputation strategy (e.g., median imputation or KNN imputation).
  * **Encoding:** Map categorical variables (`physical_activity`) and binary variables (`family_history`) into numerical formats suitable for modeling.
  * **Scaling:** Apply feature scaling (e.g., StandardScaler) since distance-based algorithms and neural networks are sensitive to unscaled data.
  * Split the dataset into Training, Validation, and Test sets.

### Phase 2: Baseline Classical Machine Learning Models
* **Objective:** Establish a performance benchmark using traditional ML algorithms.
* **Tasks:**
  * Train and tune baseline models (e.g., Logistic Regression, Random Forest, or Support Vector Machines).
  * Evaluate baseline models using cross-validation.
  * Document baseline metrics to compare against the Neural Network later.

### Phase 3: Artificial Neural Network (ANN) Development
* **Objective:** Build a Multi-Layer Perceptron (MLP) to capture the non-linear relationships in the dataset.
* **Tasks:**
  * Design the initial architecture of the ANN (input layer, hidden layers, output layer with softmax for multi-class classification).
  * Compile the model with appropriate loss functions (categorical cross-entropy) and optimizers (e.g., Adam).
  * Train the network while monitoring validation loss to watch for early signs of overfitting.

### Phase 4: Model Evaluation & Generalization Analysis
* **Objective:** Assess model performance and diagnose learning behavior.
* **Tasks:**
  * Generate **Learning Curves** (Training vs. Validation Loss/Accuracy over epochs) to identify overfitting or underfitting.
  * Evaluate models using comprehensive multi-class metrics: Accuracy, Precision, Recall, F1-Score, and Confusion Matrices.

### Phase 5: Hyperparameter Tuning & Optimization
* **Objective:** Improve the ANN's performance and generalization.
* **Tasks:**
  * Experiment with different hyperparameters (e.g., learning rate, number of hidden layers/neurons, batch size).
  * Implement regularization techniques (e.g., Dropout layers, L1/L2 regularization, or Early Stopping) if overfitting is observed in Phase 4.

### Phase 6: Final Comparison and Report
* **Objective:** Consolidate findings and draw conclusions.
* **Tasks:**
  * Compare the optimized ANN against the classical baseline models.
  * Discuss the trade-offs (e.g., performance vs. computational cost, interpretability).
  * Summarize findings in a final Jupyter Notebook or PDF report.

---

## 📁 Repository Structure (Planned)

```text
├── data/                   # Raw and processed datasets (Health_Risk_Tiers_v2.csv)
├── notebooks/              # Jupyter notebooks for EDA, modeling, and evaluation
│   ├── 01_EDA_and_Preprocessing.ipynb
│   ├── 02_Baseline_Models.ipynb
│   ├── 03_ANN_Development_and_Tuning.ipynb
├── src/                    # Python scripts for helper functions (optional)
├── docs/                   # Project descriptions, instructions, and final report
└── README.md               # Project overview and plan (This file)
