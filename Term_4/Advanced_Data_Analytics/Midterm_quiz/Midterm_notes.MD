# Advanced Data Analytics: Master Study Guide & Quiz Question Bank

## 📚 PHASE 1: CONSOLIDATED CLASS NOTES

### Module 3: Affinity Analysis & Association Rules Mining
* **Purpose:** Discovers hidden patterns/co-occurrences (e.g., Market Basket Analysis, Failure Pattern Discovery).
* **Association Rule Format:** `{Antecedent} -> {Consequent}`
* **Core Metrics:**
    * **Support:** Frequency of the rule in the dataset. Formula: `Transactions containing both A and B / Total Transactions`.
    * **Confidence:** Reliability of the rule. Formula: `Transactions containing both A and B / Transactions containing A`.
* **The Curse of Dimensionality:** With `k` attributes, the number of possible rules is `k * 2^(k-1)`.
* **Algorithms:**
    * **Apriori Algorithm:** Uses the Apriori property (if an itemset is infrequent, all supersets are infrequent) to prune the search space. Two phases: Generate frequent itemsets (filtering by minimum support threshold), then generate rules (filtering by minimum confidence).
    * **FP-Growth:** Faster than Apriori. Avoids candidate generation by compressing the database into an FP-tree structure and using a divide-and-conquer strategy.
* **Data Formats:** * *Transactional:* Two columns (Transaction ID, Item). Best for algorithms.
    * *Tabular (One-Hot Encoded):* One row per transaction, boolean columns for each item. Best for EDA.

### Module 4: Synthetic Data Generation
* **Why Use It:** Overcome data scarcity, ensure privacy/compliance (GDPR), simulate edge cases, and augment model training.
* **Types of Data:** Tabular (most common), Time Series, Image, Text.
* **Classical Methods:**
    * *Random Sampling:* Drawing from known distributions (e.g., Normal, Exponential).
    * *Bootstrapping/Permutation:* Resampling existing data with replacement.
    * *Noise Injection:* Adding controlled variations (e.g., Gaussian noise) to real values.
    * *Template-Based:* Using tools like `Faker` to generate structured dummy data based on rules.
* **Probabilistic/Statistical Models:** * *Copulas (Gaussian, Vine):* Decouple individual feature distributions from their joint dependencies to maintain correlation structures.
    * *Bayesian Modeling (PGMs):* Uses directed graphs to represent probabilistic dependencies.
* **Machine Learning Methods (SDV):**
    * *CTGAN:* GAN-based, handles categoricals and imbalanced classes well.
    * *TVAE:* VAE-based, excels at learning continuous numerical feature relationships.
    * *GaussianCopula:* Fast, interpretable statistical baseline.
* **Evaluation Dimensions:** * *Statistical Similarity:* Do distributions and correlations match?
    * *Utility:* Train on Synthetic, Test on Real (TSTR).
    * *Privacy:* Check for exact copies, disclosure risks, and data leakage.

### Module 5: Mining Data Streams
* **Stream Constraints:** Unbounded input, memory-limited, single-pass algorithms, prioritizing timeliness.
* **Query Types:** Aggregate (summaries), Frequency (tracking events), Uniqueness (cardinality estimation).
* **Window Models:**
    * *Sliding Window:* Overlapping, holds the most recent N items or time T. Updates continuously.
    * *Tumbling Window:* Non-overlapping, fixed-size batches (e.g., distinct hourly aggregations).
    * *Decaying Window (Exponential Decay):* Assigns exponentially decreasing weights to older data. Smooth trend detection without rigid cutoffs. Weight formula: `e^(-lambda * age)`.
* **Sampling & Estimation Algorithms:**
    * *Reservoir Sampling:* Maintains a uniform sample of size `k` from a stream of unknown length. New item replaces a random item with probability `k/i`.
    * *HyperLogLog (HLL):* Probabilistic distinct element counter. Hashes items and counts leading zeros. Extremely memory efficient with a bounded relative error.
* **Spark Structured Streaming:**
    * Treats streams as unbounded tables (micro-batching).
    * *Output Modes:* `Complete` (writes entire table), `Update` (writes only changed rows), `Append` (writes only new, finalized rows).

### Module 6/7: Natural Language Processing (NLP)
* **Workflow:** Text ingestion -> Preprocessing -> Feature Extraction (Vectorization) -> Machine Learning Modeling.
* **Text Preprocessing (Normalization):**
    * *Tokenization:* Splitting text into discrete units (words or sentences).
    * *Cleaning:* Lowercasing, removing punctuation, and removing Stop Words (common words like "the", "and" that add no semantic value).
    * *Stemming:* Heuristic truncation of suffixes (e.g., "running" -> "run"). Fast but crude.
    * *Lemmatization:* Uses vocabulary/morphology to reduce words to their base dictionary form (e.g., "better" -> "good"). Slower but accurate.
* **Feature Extraction (Vectorization):**
    * *Bag-of-Words (BoW):* Counts term frequencies. Ignores context and word order.
    * *TF-IDF:* Term Frequency-Inverse Document Frequency. Punishes overly common words across documents, highlighting unique, informative terms.
    * *Word Embeddings (Word2Vec, GloVe):* Dense numerical vectors that capture semantic relationships and context.
* **Machine Learning in NLP:** * Uses vectors for Sentiment Analysis, Topic Modeling, Named Entity Recognition (NER), and Text Classification. Algorithms range from Naive Bayes/SVM to deep learning (Transformers).

---

## 🧠 PHASE 2: THE QUESTION BANKS

### 🟢 EASY SET

#### Multiple Choice Questions (15)
1. **[Mod 3] What does the Support metric measure in Association Rule Mining?**
   - A) The confidence of a prediction
   - B) The frequency of an itemset in the entire dataset
   - C) The size of the FP-tree
   - D) The correlation between two independent variables
   > **Answer:** B) The frequency of an itemset in the entire dataset

2. **[Mod 3] The Apriori algorithm relies on the principle that:**
   - A) All subsets of a frequent itemset must also be frequent.
   - B) Neural networks are required for text analysis.
   - C) Streaming data must be processed in a single pass.
   - D) Rare events have higher confidence.
   > **Answer:** A) All subsets of a frequent itemset must also be frequent.

3. **[Mod 3] Which algorithm avoids candidate generation by compressing the dataset into a tree structure?**
   - A) Random Forest
   - B) FP-Growth
   - C) Naive Bayes
   - D) CTGAN
   > **Answer:** B) FP-Growth

4. **[Mod 4] Which of the following is a primary reason to generate synthetic data?**
   - A) To reduce processing speed
   - B) To increase data privacy and bypass PII regulations
   - C) To delete the original database entirely
   - D) To increase the memory footprint of Spark
   > **Answer:** B) To increase data privacy and bypass PII regulations

5. **[Mod 4] Tabular data generation typically involves simulating:**
   - A) Rows and columns of relational databases
   - B) Audio files
   - C) Pixels in an image
   - D) Natural language sentences
   > **Answer:** A) Rows and columns of relational databases

6. **[Mod 4] `Faker` is best described as a tool for:**
   - A) Machine learning vectorization
   - B) Template-based data generation
   - C) Advanced deep learning synthesis
   - D) Reservoir sampling
   > **Answer:** B) Template-based data generation

7. **[Mod 5] What characterizes a "tumbling window" in streaming analytics?**
   - A) It assigns exponential weights
   - B) It breaks the stream into non-overlapping chunks
   - C) It overlaps by 50%
   - D) It stores the entire infinite stream
   > **Answer:** B) It breaks the stream into non-overlapping chunks

8. **[Mod 5] Which algorithm is used for estimating the number of distinct elements using fixed-size memory?**
   - A) HyperLogLog
   - B) Apriori
   - C) TF-IDF
   - D) Gaussian Copula
   > **Answer:** A) HyperLogLog

9. **[Mod 5] In Spark Structured Streaming, which output mode writes only the rows that have changed?**
   - A) Append
   - B) Update
   - C) Complete
   - D) Snapshot
   > **Answer:** B) Update

10. **[Mod 6] What is the process of splitting text into individual words or sentences called?**
    - A) Stemming
    - B) Vectorization
    - C) Tokenization
    - D) Copulas
    > **Answer:** C) Tokenization

11. **[Mod 6] Words like "the", "is", and "and" that are often removed during preprocessing are called:**
    - A) Lemmas
    - B) Tokens
    - C) Stop Words
    - D) Vectors
    > **Answer:** C) Stop Words

12. **[Mod 6] Which technique chops off word endings to find the root, but may result in non-dictionary words?**
    - A) Lemmatization
    - B) Stemming
    - C) TF-IDF
    - D) Named Entity Recognition
    > **Answer:** B) Stemming

13. **[Mod 6] Bag-of-Words (BoW) evaluates text based on:**
    - A) Semantic meaning
    - B) The chronological order of words
    - C) The frequency count of words
    - D) Neural network attention
    > **Answer:** C) The frequency count of words

14. **[Mod 3] In the rule `{Bread} -> {Butter}`, `{Bread}` is the:**
    - A) Consequent
    - B) Antecedent
    - C) Support
    - D) Vector
    > **Answer:** B) Antecedent

15. **[Mod 5] A data stream model demands that algorithms ideally process data in:**
    - A) A single pass
    - B) Multiple historical batches
    - C) A relational database architecture
    - D) Encrypted text only
    > **Answer:** A) A single pass

#### Multi-Select Questions (10)
1. **[Mod 3] Which formats are commonly used to represent market basket data?**
   - [x] Transactional Format
   - [x] Tabular (One-Hot Encoded) Format
   - [ ] MP4 Format
   - [ ] JSON Graph Format
   > **Answer:** Transactional Format, Tabular (One-Hot Encoded) Format

2. **[Mod 4] Which of the following are valid dimensions for evaluating synthetic data?**
   - [x] Statistical Similarity
   - [x] Utility (TSTR)
   - [x] Privacy Risk
   - [ ] Hashing Entropy
   > **Answer:** Statistical Similarity, Utility (TSTR), Privacy Risk

3. **[Mod 5] What are standard characteristics of a stream data model?**
   - [x] Unbounded input
   - [x] Memory-limited processing
   - [ ] Ability to query the entire historical dataset freely
   - [x] Focus on timeliness
   > **Answer:** Unbounded input, Memory-limited processing, Focus on timeliness

4. **[Mod 6] Which of the following are text vectorization techniques?**
   - [x] Bag-of-Words (BoW)
   - [x] TF-IDF
   - [ ] CTGAN
   - [x] Word Embeddings
   > **Answer:** Bag-of-Words (BoW), TF-IDF, Word Embeddings

5. **[Mod 4] Which of the following models are included in the SDV library?**
   - [x] CTGAN
   - [x] TVAE
   - [x] GaussianCopula
   - [ ] HyperLogLog
   > **Answer:** CTGAN, TVAE, GaussianCopula

6. **[Mod 3] Which metrics are used to evaluate association rules?**
   - [x] Support
   - [x] Confidence
   - [ ] Lemmatization
   - [ ] Log-Loss
   > **Answer:** Support, Confidence

7. **[Mod 5] Which of the following are types of streaming windows?**
   - [x] Sliding
   - [x] Tumbling
   - [x] Decaying (Exponential)
   - [ ] Vectorized
   > **Answer:** Sliding, Tumbling, Decaying (Exponential)

8. **[Mod 4] Classical synthetic generation methods include:**
   - [x] Random sampling from distributions
   - [x] Bootstrapping
   - [x] Noise Injection
   - [ ] Variational Autoencoders (VAEs)
   > **Answer:** Random sampling from distributions, Bootstrapping, Noise Injection

9. **[Mod 6] Normalization in NLP typically includes:**
   - [x] Lowercasing
   - [x] Removing punctuation
   - [x] Removing stop words
   - [ ] Calculating Confidence
   > **Answer:** Lowercasing, Removing punctuation, Removing stop words

10. **[Mod 5] Uses for Reservoir Sampling include:**
    - [x] Getting a quick summary without full aggregation
    - [x] Feeding downstream systems that can't handle full streams
    - [ ] Generating exact distinct counts for a billion items
    - [ ] Predicting future stock prices
    > **Answer:** Getting a quick summary without full aggregation, Feeding downstream systems that can't handle full streams

#### Short Written Answer (10)
1. **[Mod 3] Define the "Curse of Dimensionality" in association rules.**
   > **Answer:** As the number of attributes increases, the number of possible item combinations and rules grows exponentially, causing severe computational expense.

2. **[Mod 4] What does "TSTR" stand for in synthetic data evaluation?**
   > **Answer:** Train on Synthetic, Test on Real.

3. **[Mod 5] Explain the difference between a sliding window and a tumbling window.**
   > **Answer:** Sliding windows overlap and update continuously, whereas tumbling windows chunk the stream into fixed, non-overlapping intervals.

4. **[Mod 6] What is the difference between Stemming and Lemmatization?**
   > **Answer:** Stemming crudely chops off word affixes, while Lemmatization uses dictionary rules to map a word back to its linguistic base form.

5. **[Mod 3] If 50 out of 100 transactions contain Milk, what is the Support of `{Milk}`?**
   > **Answer:** 50% (or 0.50).

6. **[Mod 4] Why inject noise into a dataset?**
   > **Answer:** To create slight variations of existing data, maintaining overall patterns while simulating real-world errors or preserving privacy.

7. **[Mod 5] Why is the naive approach (using a Python `set()`) bad for distinct counting in streams?**
   > **Answer:** It requires storing every unique item, leading to linear memory growth that crashes systems at a massive scale.

8. **[Mod 6] What is a "Token"?**
   > **Answer:** A distinct, atomic piece of text (usually a word or punctuation mark) split from a larger string.

9. **[Mod 4] Name one risk of ML-based synthetic data.**
   > **Answer:** Data leakage (memorizing real records), bias reproduction, or generating unrealistic artifacts.

10. **[Mod 5] What is the main benefit of HyperLogLog?**
    > **Answer:** It estimates the cardinality (distinct count) of massive datasets using a very small, fixed-size memory footprint.

#### Code Writing (10)
1. **[Mod 3] Initialize an MLxtend TransactionEncoder.**
   > **Answer:**
   ```python
   from mlxtend.preprocessing import TransactionEncoder
   te = TransactionEncoder()
