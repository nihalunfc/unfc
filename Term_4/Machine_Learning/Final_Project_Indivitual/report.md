# Comparative Analysis of Classical Machine Learning and Artificial Neural Networks for Health Risk Tier Classification

**Author:** [Your Name]  
**Institution:** [Your University/Institution Name]  
**Course:** [Course Number: Course Name]  
**Professor:** [Professor’s Name]  
**Date:** [Date]  

---

## Abstract
This project presents a comprehensive machine learning pipeline designed to classify patients into health risk tiers (Low, Medium, High) based on physiological and lifestyle factors. Utilizing the synthetic `Health_Risk_Tiers_v2` dataset, the study compares the predictive performance, generalization capabilities, and learning behaviors of classical machine learning algorithms against a deep learning approach. A Logistic Regression model was established as a linear baseline, achieving a test accuracy of 74.44%. A Random Forest classifier was utilized as a non-linear baseline, achieving the highest test accuracy at 95.56%. An Artificial Neural Network (ANN) was developed, evaluated, and optimized using L2 regularization and dropout, ultimately achieving a test accuracy of 87.78%. The results demonstrate that while the dataset contains complex non-linear relationships, tree-based ensemble models outperform deep neural networks on relatively small, structured tabular datasets.

## Declaration of Generative AI Usage
In accordance with academic transparency guidelines, generative artificial intelligence (Google Gemini) was utilized during the completion of this project. AI was employed as an interactive coding tutor to assist in debugging standard Python errors (e.g., `UnicodeDecodeError` and `ParserError` during data ingestion), structuring the initial exploratory data analysis pipeline, and formatting this final report. All architectural decisions, hyperparameter tuning evaluations, and final analytical conclusions were reviewed, executed, and validated independently by the author.

---

## Introduction
The integration of machine learning into healthcare allows for the rapid classification of patient risk based on multi-dimensional physiological data. However, the selection of the appropriate modeling algorithm is critical, as clinical data often exhibits complex, non-linear relationships. Deep learning models, such as Artificial Neural Networks (ANNs), are frequently applied to complex datasets due to their theoretical ability to approximate any continuous function. Conversely, classical models like Random Forests are often preferred for tabular data due to their robustness and interpretability. The objective of this study is to systematically preprocess a healthcare dataset, establish classical machine learning baselines, and evaluate whether a heavily optimized Artificial Neural Network can outperform a tree-based ensemble model in classifying patient health risk tiers.

## Methodology

### Dataset Description
The `Health_Risk_Tiers_v2` dataset is a synthetic healthcare dataset containing ten features and a multi-class target variable, `risk_tier`, which categorizes patients into Low Risk (0), Medium Risk (1), or High Risk (2). The feature space includes numeric variables (age, BMI, blood pressure, glucose level, sleep hours, stress level, cholesterol), categorical variables (physical activity), binary variables (family history), and a non-informative identifier (`patient_id`). 

### Data Preprocessing and Feature Engineering
To prevent data leakage and bias, rigorous preprocessing steps were executed prior to model training. The non-informative `patient_id` column was dropped. Categorical variables were encoded numerically: `family_history` was mapped to binary values (0, 1), and `physical_activity` was mapped ordinally (0, 1, 2) to preserve its inherent hierarchy (Low, Medium, High). 

The dataset was subsequently partitioned using stratified sampling to maintain class balance across all subsets: 70% for Training, 15% for Validation, and 15% for Testing. The dataset contained approximately 8% missing values exclusively within the `cholesterol` column. To address this, a Simple Imputer utilizing the median strategy was fitted solely on the training data and applied across all splits. Finally, because distance-based algorithms and neural networks are highly sensitive to feature magnitudes, standard scaling (`StandardScaler`) was applied to normalize the feature space.

### Model Architecture and Training
Three distinct models were developed to evaluate performance across linear boundaries, non-linear boundaries, and deep representations.

1. **Logistic Regression (Baseline 1):** A multinomial Logistic Regression model was initialized with a maximum of 1,000 iterations to establish a linear separability baseline.
2. **Random Forest (Baseline 2):** An ensemble consisting of 100 decision trees (`n_estimators=100`) with a maximum depth of 10 was deployed to establish a non-linear baseline.
3. **Artificial Neural Network (ANN):** A Multi-Layer Perceptron was constructed using TensorFlow/Keras. The initial architecture consisted of an input layer, two hidden layers (64 and 32 neurons utilizing ReLU activation), and a 3-neuron output layer utilizing Softmax activation for multi-class probability distribution. The model was compiled using the Adam optimizer and sparse categorical cross-entropy loss.

### Hyperparameter Tuning and Regularization
Initial ANN training resulted in visual evidence of overfitting, where validation loss diverged from training loss around epoch 30. To mitigate this, hyperparameter optimization was conducted. L2 weight regularization (Ridge) was applied to the dense layers to penalize overly large weights. The dropout rate was increased to 30% to prevent neuronal co-adaptation, and the Adam optimizer’s learning rate was reduced to 0.0005 to ensure finer gradient descent steps. An Early Stopping callback with a patience of 15 epochs was utilized to halt training when validation metrics degraded, restoring the optimal weights.

## Results

### Validation Phase Performance
During the validation phase, models were evaluated exclusively on the 15% validation split. 
* The **Logistic Regression** model achieved an overall accuracy of 78%. 
* The **Random Forest** model demonstrated vastly superior performance, achieving an accuracy of 91% and an F1-score of 0.91, indicating strong non-linear relationships within the features.
* The initial unoptimized **ANN** reached an early stopping point at epoch 42, restoring weights from epoch 32, yielding a validation accuracy of 81.1%. Following hyperparameter optimization (L2 regularization and dropout adjustments), the generalized ANN validation accuracy remained at 81%, though learning curves indicated a successful reduction in overfitting variance.

### Final Test Phase Performance
The ultimate evaluation was conducted on the 15% sequestered Test set to simulate completely unseen real-world data. The final test accuracies were as follows:

* **Logistic Regression:** 74.44%
* **Optimized ANN:** 87.78%
* **Random Forest:** 95.56%

A detailed classification report of the winning model (Random Forest) showed exceptional class recall, successfully identifying 100% of Low-Risk patients, 91% of Medium-Risk patients, and 98% of High-Risk patients.

## Discussion
The empirical results of this study illustrate several fundamental principles of machine learning application. First, the significant performance gap between Logistic Regression (74.44%) and Random Forest (95.56%) confirms that linear boundaries are insufficient for modeling human physiological risk. The interaction between variables such as BMI, glucose, and blood pressure is highly non-linear.

Second, the study highlights the limitations of Deep Learning when applied to specific data structures. While the optimized ANN successfully navigated the non-linear boundaries (outperforming Logistic Regression by over 13%), it failed to surpass the Random Forest. This supports the widely recognized consensus in data science that for structured, tabular datasets of limited size, tree-based ensemble methods generally out-compete deep neural networks. Neural networks are highly parameterized and prone to overfitting without massive quantities of data. Despite aggressive L2 regularization and dropout, the ANN could not replicate the natural variance-reduction mechanisms inherent to Random Forest bagging.

## Conclusion
This project successfully engineered a machine learning pipeline to classify patient health risks. Through methodical baseline establishment, neural network development, and hyperparameter tuning, it was determined that the Random Forest Classifier is the superior algorithm for this specific tabular dataset, yielding a test accuracy of 95.56%. Future research utilizing this dataset could explore advanced gradient-boosting frameworks (such as XGBoost or LightGBM) to determine if ensemble methodologies can be pushed closer to perfect classification.

---

## References

* Chollet, F. (2021). *Deep learning with Python* (2nd ed.). Manning Publications.
* Géron, A. (2022). *Hands-on machine learning with Scikit-Learn, Keras, and TensorFlow: Concepts, tools, and techniques to build intelligent systems* (3rd ed.). O'Reilly Media.
* Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*(85), 2825–2830.
* Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., Corrado, G. S., Davis, A., Dean, J., Devin, M., Ghemawat, S., Goodfellow, I., Harp, A., Irving, G., Isard, M., Jia, Y., Jozefowicz, R., Kaiser, L., Kudlur, M., Levenberg, J., … Zheng, X. (2015). *TensorFlow: Large-scale machine learning on heterogeneous systems*. https://www.tensorflow.org/
