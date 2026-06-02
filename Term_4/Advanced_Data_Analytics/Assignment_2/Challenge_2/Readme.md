## Business Challenge 2: Books Recommendation System

### Outline of Tasks
1. **Exploratory Data Analysis (EDA):** Summarize the dataset (rows, columns, data types), show the distribution of labels or ratings, and create at least two visualizations.
2. **Theoretical Explanation:** Write a summary explaining the Alternating Least Squares (ALS) model, how it uses matrix factorization, and its main hyperparameters.
3. **Data Preparation:** Convert the dataset into a user-item interaction matrix.
4. **Model Training:** Fit the ALS model using the implicit library on the training set and explicitly report factors, regularization, iterations, and other key parameters.

### Requirements
* **Environment:** Jupyter Notebook.
* **Libraries:**
  * `pandas` and `matplotlib`/`seaborn` (for EDA).
  * `scipy.sparse` (to create the user-item matrix).
  * `implicit` (to access the ALS model; requires running `pip install implicit`).

### Dataset Information
* **Dataset:** Goodbooks-10k dataset (contains over 6 million ratings from 50,000+ users on 10,000 unique books).
* **Source:** Download via the hyperlink provided in the assignment document.

### Summary of Action Plan
For the second challenge, I will develop a collaborative filtering recommendation engine. After exploring the book ratings data, I will transform the raw dataset into a sparse user-item matrix. Then, I will train an Alternating Least Squares (ALS) model using the implicit library to identify similar books and predict recommendations based on underlying patterns in past user ratings.
