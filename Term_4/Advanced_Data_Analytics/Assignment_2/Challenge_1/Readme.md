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
* **Dataset:** Yelp Dataset. *https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset*
* **Source:** Check the university course portal for the provided data files or locate the official Yelp Open Dataset online.

### Challenge 1: Yelp Sentiment Analysis Tracker

| Phase | Task | Description | Status |
| :--- | :--- | :--- | :--- |
| **1. Setup** | Data Ingestion | Load the Yelp dataset into a Pandas DataFrame and inspect the schema. | [ ] Pending |
| **2. EDA** | Class Imbalance | Calculate and visualize the ratio of positive to negative reviews. | [ ] Pending |
| **2. EDA** | Review Extraction | Sample and display representative positive and negative text strings. | [ ] Pending |
| **2. EDA** | Length Distribution | Plot the distribution of review text lengths to inform text tokenization. | [ ] Pending |
| **3. Baseline** | Model Build | Vectorize text using TF-IDF and train an initial Random Forest classifier. | [ ] Pending |
| **3. Baseline** | Evaluation | Generate a classification report (precision, recall, F1, support) and a confusion matrix. | [ ] Pending |
| **4. Optimization** | Grid Search Setup | Configure hyperparameter grid (estimators, depth, min_samples_split, min_samples_leaf, max_features). | [ ] Pending |
| **4. Optimization** | Tuning | Execute the grid search to find the optimal configuration for the Random Forest model. | [ ] Pending |
| **4. Optimization** | Business Insight | Document the chosen hyperparameters and explain their importance for business decision-making. | [ ] Pending |
| **5. Advanced ML** | Transformer 1 | Implement the first pretrained Hugging Face transformer model for sentiment classification. | [ ] Pending |
| **5. Advanced ML** | Transformer 2 | Implement the second pretrained Hugging Face transformer model. | [ ] Pending |
| **5. Advanced ML** | Evaluation Compare| Compare the performance of both transformers against the optimized baseline model. | [ ] Pending |
| **5. Advanced ML** | Business Value | Quantify the impact (e.g., reducing false negatives) and translate it to actionable service quality improvements. | [ ] Pending |
| **6. Delivery** | Final Review | Ensure the Jupyter Notebook is clean, well-commented, and structurally ready for submission. | [ ] Pending |
