**Assignment 2: Analytical Model Choice and Customer Segmentation**

 

Group 5: Gerald Abbey, Olamide Ibukunoluwa Yusuf, Nihal Vellaramkallingal Sulaiman and Souren Chowdhury.

**Machine Learning** 

**Master of Data Analytics, University of Niagara Falls Canada**

 

 

**Instructor: Touraj Banirostam**


 

**May 23, 2026**

**Part A – Pre-Analysis and Hypotheses**

**Model Family Expectation**

Prior to experimental execution, we hypothesize that the ensemble model family, specifically the Random Forest classifier, will yield superior predictive performance compared to the Support Vector Machine (SVM). The *Retail\_Customer\_Insights\_v2* dataset comprises mixed data types, including continuous numerical variables (e.g., average transaction value) and categorical variables (e.g., region, preferred channel). Tree-based ensemble methods are inherently well-suited for heterogeneous data, as they partition feature spaces using orthogonal decision boundaries and do not rely on strict geometric distance metrics. Conversely, SVMs map data points into a high-dimensional continuous space; the introduction of one-hot encoded categorical variables often introduces sparsity and noise, which can degrade the effectiveness of the Radial Basis Function (RBF) kernel without exhaustive tuning.

**Appropriate Evaluation Metrics**

In the context of customer churn prediction, relying exclusively on accuracy as an evaluation metric is fundamentally flawed. Churn datasets exhibit inherent class imbalance, as the majority class represents retained customers while the minority class represents those who churn. If a dataset contains 90% retained customers, a naive model that predicts "No Churn" for every instance would achieve 90% accuracy while failing entirely at its actual business objective. Therefore, the F1-score—the harmonic mean of Precision and Recall—is the most appropriate primary metric. It balances the model's ability to capture actual churners without generating excessive false positive flags. Furthermore, ROC-AUC will be utilized to measure the model's discriminative threshold stability.

**Expected Segmentation Structure**

For the unsupervised learning phase, we anticipate discovering distinct behavioral archetypes driven by transactional recency, frequency, and monetary value. We expect the clustering algorithms to separate the customer base into actionable business segments, such as a "High-Value Loyal" cohort characterized by high spend and frequent interactions, contrasted against an "At-Risk/Disengaged" cohort marked by declining frequency and low transaction values.

**Part B – Experimental Design**

**Data Splitting and Preparation**

To ensure a robust and unbiased evaluation of the predictive models, the dataset was partitioned using a 70/30 train-test split. To maintain the representative distribution of the minority churn class across both sets, the split was strictly stratified based on the target variable (churn\_risk). A fixed random seed (42) was applied across all algorithmic initializations to guarantee experimental reproducibility.

**Preprocessing Strategy**

The preprocessing pipeline was designed to handle data inconsistencies while preventing data leakage. The customer\_id feature was immediately dropped, as unique identifiers hold no generalized predictive power. Missing values in continuous features were addressed using median imputation, a strategy selected for its robustness against extreme outliers that skew mathematical averages. Categorical variables, such as region and preferred channel, were transformed using one-hot encoding.

Crucially, all feature scaling (Standardization) and encoding were encapsulated within a Scikit-Learn ColumnTransformer and Pipeline. During the 5-fold cross-validation phase on the training set, this pipeline ensures that standard scaling is fit exclusively on the *k-1* training folds and merely applied to the validation fold. This prevents information from the validation data from improperly influencing the scaling parameters of the training data.

**Part C – Classification Analysis**

**Model Training and Hyperparameter Tuning**

Following the assignment constraints, two distinct models were evaluated: a Random Forest (Ensemble) and an SVM utilizing an RBF kernel. Hyperparameter optimization was restricted to a single parameter per model, evaluated across three specific values using 5-fold cross-validation optimized for the F1-score.  
For the Random Forest, we tuned the number of trees (n\_estimators) evaluating values of \[50, 100, 200\]. For the SVM, we tuned the regularization parameter (C), evaluating values of \[0.1, 1.0, 10.0\]. The cross-validation process revealed distinct differences in stability. The Random Forest model demonstrated consistently lower variance (standard deviation) across the five validation folds. The SVM exhibited higher sensitivity to the variation in the subsets, heavily reliant on the optimal selection of the C penalty parameter to balance the margin width against misclassification tolerances.

**Performance and Stability Analysis**

When evaluated on the unseen 30% test set, the Random Forest model outperformed the SVM across all primary metrics, including F1-Score, Recall, and ROC-AUC.

The performance disparity can be attributed to the algorithmic architecture of both models. The Random Forest benefits from bagging (bootstrap aggregating), where multiple decision trees are trained on random subsets of data and features. This averaging mechanism heavily suppresses the model's overall variance and prevents overfitting to the noise inherent in retail behavior data.  
The SVM's relative underperformance highlights its vulnerability to high-dimensional categorical encoding. The RBF kernel measures the Euclidean distance between data points in a transformed space. When categorical variables are expanded into multiple binary columns via one-hot encoding, it artificially inflates the dimensionality of the feature space, making distance calculations less meaningful—a phenomenon related to the curse of dimensionality.

**Business Perspective and Error Costs**

In the commercial landscape of churn management, classification errors carry distinct financial weights. A False Positive occurs when a loyal customer is incorrectly flagged as a churn risk; the associated cost is relatively low, typically limited to the margin lost by offering them an unnecessary retention discount. A False Negative, however, occurs when a genuinely at-risk customer is missed by the model. The cost of a False Negative is severe: the permanent loss of the customer's future lifetime value and the high marketing acquisition cost required to replace them.

Because False Negatives are substantially more expensive, maximizing Recall (the ability to find all actual true churners) is a critical business imperative, even if it requires a slight compromise in Precision.

**Deployment Recommendation**

Based on analytical and commercial evidence, the Random Forest model is recommended for production deployment. Not only does it yield higher discriminative power (superior ROC-AUC) and operational stability (lower cross-validation variance), but it also natively supports probability outputs. In a production environment, the business can dynamically lower the prediction probability threshold below 0.5 to intentionally capture more at-risk customers, directly optimizing for the high cost of False Negatives.

**Part D – Unsupervised Learning and Segmentation**

**Methodology and Assumptions**

To uncover inherent customer structures without relying on predefined labels, we applied K-Means and DBSCAN clustering algorithms to the fully scaled dataset. These algorithms operate on fundamentally different mathematical assumptions. K-Means assumes that data clusters are convex, spherical, and relatively similar in density; it is a partition-based algorithm that forces every single data point into a designated cluster.  
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) operates on contiguous areas of high point density, separated by areas of low density. Unlike K-Means, DBSCAN does not force every point into a cluster; if a customer’s behavioral data points do not fall within a dense neighborhood defined by the epsilon (eps) parameter, they are labeled as noise.

**Clustering Evaluation**

K-Means was evaluated across *k* values of 2, 3, 4, and 5\. Model cohesion and separation were measured using the Silhouette Score, which calculates how closely matched a data point is to its own cluster compared to neighboring clusters.

DBSCAN was evaluated across multiple epsilon distances. The primary finding from the DBSCAN analysis was its categorization of a massive percentage of the dataset as unclustered noise. This outcome provides a critical insight into the topology of the data: retail customer behavior in this dataset does not form tightly isolated "islands" of similarity. Instead, spending patterns, recency, and frequency exist on a fluid, continuous spectrum.

**Algorithm Suitability and Business Interpretation**

From a practical business perspective, K-Means is significantly more useful for this dataset. Customer Relationship Management (CRM) requires exhaustive segmentation; marketing departments need to assign every customer to a specific campaign track. DBSCAN’s strict density requirements resulted in an unusable amount of noise points, leaving vast portions of the customer base untargetable.

By applying K-Means, we successfully divided the continuous spectrum of data into actionable commercial segments. Analyzing the centroids of the optimal K-Means clusters reveals distinct consumer archetypes. For instance, we can identify a segment representing "High-Value Loyal" customers, defined by above-average transaction values and high frequency. Conversely, another distinct segment represents "Disengaged" customers, marked by low monetary value and high recency gaps since their last transaction. These forced partitions, while mathematically less organic than density-based clusters, provide the exact structured framework required for modern, targeted marketing operations.

**AI Tool Use Disclosure**

During the execution of this assignment, artificial intelligence (Copilot) was utilized strictly as an analytical sounding board and formatting assistant. All experimental design decisions, hyperparameter selections, and algorithmic hypotheses were uniquely generated by the human group members. Specifically, AI was used to review our Python Pipeline architecture to ensure it adhered to best practices for preventing data leakage during cross-validation. Additionally, after synthesizing our raw outputs and business interpretations, the AI was prompted to assist in formatting our findings into this final, structurally coherent APA document to meet the length and clarity requirements of the grading rubric. No AutoML tools were utilized to generate the models or execute the code.  
