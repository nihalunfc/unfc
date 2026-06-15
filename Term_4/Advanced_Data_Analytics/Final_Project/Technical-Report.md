# Technical Report: Maximizing Guest Retention through Cross-Property Analytics
**Course:** DAMO630 – Advanced Data Analytics (Master of Data Analytics, UNF Canada)
**Authors:** Nihal, Gerald, Ansu, Souren

---

## 1. Introduction and Problem Statement
The hospitality industry, particularly large hotel conglomerates, faces significant revenue leakage due to late-stage booking cancellations. Traditionally, hotel management systems view guest data in silos—analyzing room reservations completely separately from point-of-sale (POS) data at on-property amenities like casinos, spas, and fine dining restaurants. 

This siloed approach blinds management to a guest's true engagement level. Our problem statement addresses this gap: **How can we integrate cross-property behavioral data to predict when a guest will cancel, and how can we automate targeted interventions to save at-risk revenue?**

Our objective is to engineer an end-to-end cloud analytics pipeline that tests the hypothesis that guests with cross-property engagement exhibit lower churn rates. Furthermore, we aim to build an automated recommendation engine that leverages Natural Language Processing (NLP) to prescribe personalized retention offers.

## 2. Related Work
Historically, churn prediction in hospitality relies on basic logistic regression models utilizing booking lead time and deposit types to predict binary cancellation outcomes (Antonio et al., 2017). However, these models fail to account for the *timing* of the cancellation. 

Our approach applies **Survival Analysis (Kaplan-Meier Estimators)**—a technique predominantly used in healthcare and telecommunications—to the hospitality sector. By modeling "time-to-cancellation," we can identify exact temporal risk windows. Additionally, instead of using black-box collaborative filtering (like ALS) for upselling, we utilize **Lexicon-based Sentiment Analysis** to build a highly interpretable, rule-based Recommendation Engine. This ensures that marketing interventions are contextually appropriate, avoiding the common pitfall of upselling a guest who recently had a negative experience.

## 3. Data Preparation and Cloud Setup
To ensure scalability and reproducibility, the entire project was developed within a **Databricks Cloud environment**, utilizing PySpark for distributed data processing and GitHub for version control.

Because proprietary conglomerate transaction logs are strictly guarded, we engineered a "Hub and Spoke" data architecture to seamlessly blend real and synthetic data:
* **The Hub (Core Bookings):** We ingested the Kaggle *Hotel Booking Demand* dataset (~119,000 rows), assigning a unique `Guest_ID` to establish a primary key.
* **Spoke 1 (NLP Reviews):** We ingested the Kaggle *TripAdvisor Hotel Reviews* dataset. Using a PySpark `LEFT JOIN`, we randomly mapped these reviews to a subset of our `Guest_ID`s, accurately simulating the real-world reality that only a fraction of guests leave written feedback.
* **Spoke 2 (Synthetic Spend Generation):** To satisfy the Synthetic Data Generation module, we utilized the Python `Faker` library to simulate highly realistic, timestamped POS transactions across various property amenities (Casino, Spa, Dining) for our specific `Guest_IDs`.

To prevent data duplication during the final join, PySpark was used to aggregate the synthetic spending logs into single-row summary features (`Total_Extra_Spend`, `Total_Transactions`) before saving the unified dataset as a permanent Delta Table (`default.final_table`).

## 4. Methodology
Our pipeline executes three distinct advanced analytics modules:

**A. Exploratory Data Analysis (EDA):**
We utilized Pandas, Matplotlib, and Seaborn to establish baseline churn metrics. We engineered features such as `Lead_Time_Months` and `Spender_Category` to visualize the macro-relationships between prepayments, booking distance, and cancellation volume.

**B. Survival Analysis (Predicting Churn Timing):**
We utilized the `lifelines` Python library to calculate Kaplan-Meier survival curves. 
* **Duration Variable:** `lead_time` (Days between booking and arrival).
* **Event Variable:** `is_canceled` (Boolean churn indicator).
We split the data into two distinct cohorts: *On-Property Spenders* vs. *No Extra Spend* to mathematically compare their retention probabilities over time.
*The retention probability over time is mathematically evaluated using the Kaplan-Meier estimator.
* Let $t_1 < t_2 < \dots < t_k$ be the distinct points in time where at least one booking cancellation occurred. The probability of a booking surviving past time $t$ is calculated as:
$$S(t) = \prod_{i: t_i \le t} \left(1 - \frac{d_i}{n_i}\right)$$
*Where:$d_i$ represents the number of distinct cancellations (events) occurring at time $t_i$.$n_i$ represents the total number of active, un-canceled bookings surviving just prior to $t_i$.

**C. NLP Sentiment Analysis & Recommendation Engine:**
Using the `TextBlob` library, we deployed a PySpark User-Defined Function (UDF) to extract polarity scores (-1.0 to 1.0) from the historical review text. We then built a prescriptive logic engine:
* **Sentiment < 0:** Triggers an automated "Service Recovery" offer (e.g., 20% off next stay) to prevent permanent churn.
* **Sentiment > 0:** Scans for specific amenity keywords (e.g., "massage", "poker") to trigger a "Targeted Upsell" (e.g., Spa or Casino credits).

## 5. Results and Analysis

**1. Baseline EDA Results:**
Our initial analysis confirmed industry standards: bookings made further in advance carry a significantly higher baseline risk of cancellation. Furthermore, non-refundable deposits act as a near-perfect barrier to churn.

**2. Survival Analysis Insights:**
<img width="1014" height="624" alt="KP" src="https://github.com/user-attachments/assets/b479ef21-990e-48b5-b84a-46280924d650" />

The Kaplan-Meier curves validated our core business hypothesis. The "On-Property Spenders" cohort maintained a significantly higher probability of retaining their reservations across all time horizons compared to standard room-only bookings. The steepest drop-offs in the survival curve revealed the specific "high-risk windows" (e.g., 30 days and 14 days out) where standard bookings are most vulnerable to cancellation.

**3. NLP Engine Efficacy:**
<img width="859" height="547" alt="sentiment" src="https://github.com/user-attachments/assets/5192cfc1-12c0-4ef7-aaba-b35f3c48eb8e" />
<img width="1152" height="547" alt="offer" src="https://github.com/user-attachments/assets/c72cbdc6-90e9-411c-b398-bf8138bfebd4" />

The NLP engine successfully segmented our audience. The output visualizations demonstrate the engine's ability to isolate the specific volume of dissatisfied guests requiring service recovery, while intelligently distributing high-margin upsells to the positively-scored majority based on their demonstrated textual interests.

## 6. Limitations
* **Synthetic Data Assumptions:** While our `Faker` script generated highly realistic spending distributions, the core correlation between spending and survival was built on a synthetic assumption. If applied to real-world proprietary POS data, the precise retention margins may vary. However, the *architecture* is perfectly built to ingest real data immediately.
* **Lexicon NLP Constraints:** `TextBlob` relies on predefined word dictionaries. It can occasionally misclassify sarcasm or complex negative phrasing. Future iterations could integrate LLMs (e.g., BERT) for deeper contextual understanding.

## 7. Business Recommendations
Based on our cloud analytics pipeline, we prescribe the following actionable recommendations for hotel conglomerates:

1. **Implement Lead-Time Triggered Marketing:** Management should abandon generic "batch-and-blast" emails. Instead, marketing automation should be synced with our Kaplan-Meier survival curve, triggering targeted incentives strictly to room-only guests 48 hours before they hit their highest-risk cancellation windows.
2. **Automate Service Recovery:** Integrate our NLP module into the central feedback system. By automatically issuing recovery discounts to negative-sentiment guests within minutes of review submission, the hotel can intercept churn before the guest books with a competitor.
3. **Break Down Data Silos:** To achieve true Customer Lifetime Value (CLV), hotel IT infrastructure must bridge the gap between the Central Reservation System (CRS) and amenity Point-of-Sale (POS) systems. As proven by our models, knowing what a guest does *outside* their room is the key to keeping them *in* it.

## 8. Data Sources

* **Hotel Booking Demand:** Christensen, J. (2019). *Hotel booking demand*. Kaggle. https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
* **Trip Advisor Hotel Reviews:** Alam, M. (2020). *Trip Advisor Hotel Reviews*. Kaggle. https://www.kaggle.com/datasets/andrewmvd/trip-advisor-hotel-reviews
