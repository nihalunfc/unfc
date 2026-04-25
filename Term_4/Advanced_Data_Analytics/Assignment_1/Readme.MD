# Assignment_1
## Nihal, Ansu, Souren and Gerald


### Assignment 1: Status Tracker

| Challenge | Task | Description / Deliverable | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Task I: EDA** | Load data, report distributions (num + cat) | DONE| Needs plots for `HealthInsurance.csv` |
| | | Highlight privacy-sensitive attributes | INCOMPLETE | Write markdown in notebook |
| | | Visualize correlations between features | INCOMPLETE | Correlation heatmap |
| | **Task II: Baseline** | Apply classical method (Faker/Bootstrapping) | INCOMPLETE | Implemented Bootstrapping |
| | | Compare real vs. synthetic distributions | INCOMPLETE | Side-by-side histograms |
| | | Discuss strengths/limitations | INCOMPLETE | Write markdown in notebook |
| | **Task III: SDV** | Train CTGAN on real dataset | INCOMPLETE | May take time to run |
| | | Train Gaussian Copula on real dataset | INCOMPLETE | |
| | | Generate synthetic datasets | INCOMPLETE | |
| | | Compare statistical similarity | INCOMPLETE | Use SDV Evaluation framework |
| | **Task IV: Eval** | Statistical similarity (KS test, correlations) | INCOMPLETE | |
| | | Utility (TSTR: Train Synth, Test Real) | INCOMPLETE | ML classification/regression test |
| | | Privacy (Row-level duplication check) | |INCOMPLETE | |
| | | Business interpretation (Markdown) | INCOMPLETE | Write conclusion for startup |
| 2 | **Task I: Setup** | Upload taxi data to HDFS / Cloud | DONE | Bash/HDFS commands |
| | | View contents in HDFS | INCOMPLETE | |
| | | PySpark: Schema, row count, sample records | INCOMPLETE | |
| | | PySpark: Basic stats (avg fare, dist, passengers) | INCOMPLETE | |
| | **Task II: MapReduce**| Compute total fare revenue per pickup location | INCOMPLETE | Implement Mapper & Reducer |
| | | Display partial outputs (map, shuffle, reduce) | INCOMPLETE | |
| | | Discuss MapReduce vs. Spark limitations | INCOMPLETE | Write markdown in notebook |
| | **Task III: FPGrowth**| Treat trip as basket (pickup, dropoff, time) | INCOMPLETE | Data transformation step |
| | | Apply FPGrowth algorithm | INCOMPLETE | |
| | | Report top 10 rules (support, confidence, lift) | INCOMPLETE | |
| | | Interpret urban mobility insights | INCOMPLETE | Write markdown in notebook |
| | **Task IV: KMeans** | Segment by avg dist, avg fare, time-of-day | INCOMPLETE | VectorAssembler & KMeans |
| | | Report cluster centers as rider personas | INCOMPLETE | |
| | | Suggest tailored services/pricing | INCOMPLETE | Write markdown in notebook |
