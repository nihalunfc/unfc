# DAMO630 – Advanced Data Analytics: Final Project
## Maximizing Guest Retention through Cross-Property Analytics

**Master of Data Analytics** **University of Niagara Falls, Canada** **Due:** 14 June 2026 

---

## Project Overview
This repository contains the end-to-end cloud analytics pipeline and deliverables for our Advanced Data Analytics final project. By integrating synthetic point-of-sale data with real-world hotel booking and review datasets, this project applies Survival Analysis and Natural Language Processing to predict guest churn and recommend automated, personalized retention strategies.

---

## Repository Structure & File Descriptions

* **`Technical-Report.md`**: The comprehensive technical document covering our problem statement, methodology, cloud setup, analysis of results, limitations, and actionable business recommendations.
* **`Business-Presentation.pdf`**: The executive slide deck summarizing our key insights, visualizations, and financial recommendations tailored for a non-technical audience.
* **`Data-Pipeline.ipynb`**: The Databricks/PySpark notebook responsible for ingesting the Kaggle datasets, utilizing the `Faker` library for synthetic POS data generation, and cleaning the final dataset, the core analytics containing our exploratory data analysis (EDA), Kaplan-Meier survival curves, and the text-processing NLP engine.
* **`output.html`**: A static HTML export of our final Databricks notebook execution for quick browser-based viewing of our visualizations and code outputs.
* **`requirements.txt`**: A list of all specific Python dependencies (e.g., `lifelines`, `TextBlob`, `Faker`) required to reproduce our environment.

---

## Team Delegation & Individual Contributions

* **Nihal:** Lead Data Engineer. Designed the Databricks architecture, authored the `Data-Pipeline.ipynb` code, and built the synthetic data generation module. 
* **Gerald:** Lead NLP & Recommendation Developer. Authored the sentiment analysis UDFs and rule-based recommendation logic within the analytics notebook, and co-wrote the Related Work section of the report.
* **Ansu:** Lead Predictive Modeler. Built and evaluated the Kaplan-Meier and Cox Proportional Hazards models for the Survival Analysis module, and authored the Methodology and Results sections of the report.
* **Souren:** Lead Business Intelligence & Communications. Developed the final business-oriented visualizations, authored the executive Business Presentation, and formatted the final Technical Report to ensure alignment with business value.
