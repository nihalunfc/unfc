# Spring 2026 Machine Learning (DAMO-640-10)
*Prof. Touraj Banirostam*

This folder contains all my notes,exercises and test files for the ML course aling with the keynotes, classnotes etc.
## Classnotes Week 1
*14 April 2026, 1PM - 3PM*

### Supervised Learning (Classification)
#### Classification vs. Regression
Classification: The output variable is categorical. The goal is to assign eac input instance to one of the fixed category. \
example: 
1. Email spam detection: Based on the presence of certain keywords, the email will be categorised into "spam" or "not spam"
2. Medical Diagnosis:
3. Sentiment Analysis: Classifies customer reviews as "positive" or "negative"
*Classification problems can be binary or multi-class.*
**Algorithms used:** Decision Trees, Random Forests, Logistic Regression, Support Vector Macchines, Naive Bayes.
##### Difference between Classification and Regression
#### Theory and Structure
1. Decision tree components:  Features root, internal and leaf nodes (branches). Most ccases, each nodes have 2 branches and so on. 
2. Splitting Metrics: ENtropy and Gini impurity measures data purity to determine the best splits in a tree model.
3. Information Gain and Splitting:
##### What is Entropy?
Measure of uncertainity, randomness or impurity in a dataset. It quantifies the expected amountinformation (or surprise) contained in a message. In Classification tasks, it measures how mixed the classes are in a particular subset of the data. 
C is the number of classes, p<sub>1</sub> is th eproportion of data points in class 1 in node 1. 
$H(t) = - \sum_{i=1}^{c} p_i \log_2(p_i)$
##### What is Information gain?
##### What is Gini?
It is a number that tells us how mixed or impure a group of data is. Low gini means group is more pure. (mostly one label). High gini means, group is more mixed. 
##### Overfitting in decision tree
A model learns the training data too well, including its noise, errors or random fluctuations. Instead of learning but memorises things and once it runs on testing data, the results is very poor, around 75% or less accuracy though it might have been 100% accurate in training. 
**Occurs when:**
1. Grows too deep or has too many branches.
2. Tries to perfectly classify the data.
3. Captures noise, outliers all perfectly. 
###### Implementation and Overfitting
Hyperparameters can be adjusted to fine-tune the accuracy. 
1. Random Forests: COmbines many decision trees to make better predictions, instead of relying on just one tree. It multiple trees using random parts of the data and then ombines their results.
2. For classification, it picks the answer the most trees agrees on.
3. For regression, it takes the average of all the tree predictions.
4. This approach will helps in improving accurance, reducing overfitting, make the model more better on new data. This randomness in both data and features make the model more robust and perfectly trained.
###### Parameters and Hyperparameter in ML
| Feature | Model Parameters | Model Hyperparameters |
| :--- | :--- | :--- |
| **Definition** | Internal configuration learned from data | External configuration set by the user |
| **How they're set** | Learned automatically during training | Manually specified before training |
| **Purpose** | Used to make actual predictions | Used to control the learning process |
| **Estimated by** | Optimization algorithms (e.g., Gradient Descent) | Tuning techniques (e.g., Grid Search, Random Search) |
| **Examples** | Weights, biases, coefficients, support vectors | Learning rate, epochs, batch size, tree depth |
| **Dependence** | Data-dependent | Problem-dependent |

#### Logistic Regression
##### Implementations and Limitations
1. Model Implementation steps
2. Working Mechanisms:
3. Assumption and Limitations: 
4. Practical Use Cases:
##### Limitations of Logistics Regression
1. Assumes lienarity
2. Not ideal for complex, non linear problems
3. Can struggle with unbalanced datasets
4. Not as powerful as tree based models

## Classnotes Week 2 
*14 April 2026, 1PM - 3PM*

## Classnotes Week 3
*21 April 2026, 1PM - 3PM*

1. Confusion matrix - false positive, true positive, false negative and true negative
2. Key classification metrics: Accuracy = Proportion of correct preditions out of the total predictions made by the model.
3. Area Under the ROC Curve (AUC) - TPR, FPR,AUC,ROC, Definition, Range and Perforrmance.
4. Cross validation Techniques: K-Fold, Stratified K-Fold,LOOCV,Holdout method
5. Overfitting and challenges
6. Hyperparameter tuning approaches

## Classnotes Week 4
*28 April 2026, 1PM - 3PM*

1. Dimensionality
2. Dimensionality reduction - Feature selection, Feature extraction
3. Key techniques - PCA - principal component analysis and LDA - Linear Discriminant Analysis
4. How PCA Works? (billconnelly.net/?p=697)
5. LDA
6. Feature selection - Methods of feature selection - Filter Methods and Wrapper Methods, evolutionary computing for large datasets
7. Feature extraction -
8. Curse of dimensionality
9. mentimeter time
