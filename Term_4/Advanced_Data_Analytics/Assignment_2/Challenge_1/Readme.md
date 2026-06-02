## Business Challenge 1: Yelp Customer Sentiment Analysis

### Outline of Tasks
1. **Exploratory Data Analysis (EDA):** Assess whether there is a class imbalance, extract and display sample reviews from both positive and negative categories, and plot the distribution of review lengths.
2. **Baseline Model Construction:** Develop a baseline sentiment classifier using TF-IDF and a Random Forest algorithm.
3. **Baseline Evaluation:** Generate a validation report showing precision, recall, F1-score, and support, alongside a confusion matrix on the validation data.
4. **Model Optimization:** Run a grid search to improve the baseline by tuning the number of estimators, maximum tree depth, minimum samples split, minimum samples per leaf, and maximum features.
5. **Advanced Modeling:** Implement two pretrained transformer models from Hugging Face for sentiment classification.
6. **Comparison and Business Value:** Compare the transformer models against the optimized Random Forest model and explain the business impact, such as how better precision or fewer false negatives affects service quality.

### Requirements
* **Environment:** Jupyter Notebook.
* **Libraries:** 
  * `pandas` and `matplotlib`/`seaborn` (for EDA).
  * `scikit-learn` (for TF-IDF, Random Forest, Grid Search, and evaluation metrics).
  * `transformers` (Hugging Face, for pretrained models).

### Dataset Information
* **Dataset:** Yelp Dataset.
* **Source:** Check the university course portal for the provided data files or locate the official Yelp Open Dataset online.

### Summary of Action Plan
For this first challenge, my goal is to build an automated sentiment classification pipeline. I will start with traditional machine learning to establish a solid baseline, optimize it via grid search, and then deploy cutting-edge pretrained transformer models to measure performance improvements. Finally, I will translate these technical metrics into actionable business insights.
