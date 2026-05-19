# Clustering Analysis: Iterative Comparison of K-Means++ and K-Medoids

This repository provides a deep dive into unsupervised grouping models, visualizing how **K-Means++** and **K-Medoids** process data points iteratively and handle heavy datasets populated with extreme outliers.

---

## Convergence Breakdown

The generated layout below demonstrates how the centers shift across their individual calculation tracks until convergence is fully achieved. 

![Clustering Convergence Process](clustering_animation.gif)

### Key Structural Differences to Notice:
1. **Mathematical Representation:** Notice that K-Means++ uses a calculated mathematical mean (the red **X**). It rests in virtual coordinate space where no physical data point exists. K-Medoids (the cyan **Diamond**) is hard-locked to an actual dataset row at every single iteration step.
2. **Outlier Pull:** Pay close attention to the rightmost cluster. The K-Means++ centroid is dragged outward to the right by the small group of extreme outlier dots. K-Medoids ignores this leverage and remains anchored inside the cluster's high-density core.

---

## Setup and Reproduction Instructions

### Environment Configuration

Use standard pip syntax to provision the math and graphics packages required by the engine:

```bash
pip install numpy matplotlib scikit-learn pillow
```

### Execution

Save the project script to your working environment as `animate_clusters.py` and run it from your terminal:

```bash
python animate_clusters.py
```

The script execution will open an interactive plotting window and automatically generate a high-resolution file named `clustering_animation.gif` inside your local directory. Commit and push this new file alongside your source code to render it on 
