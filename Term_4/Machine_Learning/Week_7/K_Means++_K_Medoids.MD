# Clustering Analysis: K-Means++ vs. K-Medoids

This project provides a visual and conceptual comparison between **K-Means++** and **K-Medoids** clustering algorithms, demonstrating how they handle datasets containing extreme outliers.

---

## Key Differences


| Feature | K-Means / K-Means++ | K-Medoids |
| :--- | :--- | :--- |
| **Cluster Center** | Mathematical average (virtual centroid) | An actual, pre-existing data point (medoid) |
| **Outlier Sensitivity** | High (outliers pull the center toward them) | Low (robust to extreme noise) |
| **Distance Metric** | Strictly requires Euclidean distance | Works with any custom dissimilarity measure |
| **Scalability** | Fast and highly scalable to large datasets | Slower due to intensive pairwise calculations |

---

## Interactive Visualizations

To see how these algorithms iteratively shift and adjust their boundaries to lock onto clusters, you can observe these dynamic step-by-step models:

* **K-Means Convergence:** View the dynamic step-by-step shifts on [Wikimedia Commons](https://wikimedia.org), which animates how cluster boundaries change across multiple iterations from an unfavorable starting position.
* **K-Medoids Step-by-Step Build:** Explore the visual iteration structure on this [Medium Guide by Prasanth](https://medium.com), illustrating how the algorithm systematically tests actual data points to minimize total cluster distance.

---

## Static Comparison Output

Once you run the script provided below, it will export a high-resolution comparison plot showcasing the impact of outliers on both algorithms.

![Clustering Comparison](clustering_comparison.png)

### Key Observations in the Visual Plot:
* **Center Placement:** K-Means++ calculates a virtual average (marked as a red **X**) that sits in empty space. K-Medoids anchors directly onto a real data point (marked as a cyan **Diamond**).
* **The Outlier Effect:** On the far-right cluster, the red K-Means center is dragged visibly further to the right due to the artificial anomalies. The cyan K-Medoids center resists this drag and stays firmly rooted in the dense core of the actual cluster.

---

## Getting Started

### Prerequisites

Install the required dependencies using `pip`:

```bash
pip install numpy matplotlib scikit-learn scikit-learn-extra
```

### Python Implementation Script

Run the following script to generate the synthetic data, perform the clustering, and automatically export the comparison image.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids

# 1. Generate synthetic data with 3 distinct groups
np.random.seed(42)
group1 = np.random.normal(loc=[1, 1], scale=0.5, size=(50, 2))
group2 = np.random.normal(loc=[5, 5], scale=0.6, size=(50, 2))
# Group 3 includes extreme outliers to show the difference
group3 = np.random.normal(loc=[9, 2], scale=0.5, size=(45, 2))
outliers = np.array([[14, 2], [14.5, 2.5], [15, 1.5]])  
X = np.vstack([group1, group2, group3, outliers])

# Define number of clusters
k = 3

# 2. Fit K-Means++ 
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)
kmeans_centers = kmeans.cluster_centers_

# 3. Fit K-Medoids
kmedoids = KMedoids(n_clusters=k, random_state=42)
kmedoids_labels = kmedoids.fit_predict(X)
kmedoids_centers = kmedoids.cluster_centers_

# 4. Plot the comparison side-by-side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Left Plot: K-Means++
ax1.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis', alpha=0.6, edgecolors='k')
ax1.scatter(kmeans_centers[:, 0], kmeans_centers[:, 1], c='red', marker='X', s=250, 
            label='Calculated Centroids\n(Virtual Average)', edgecolors='black')
ax1.set_title('K-Means++ Clustering', fontsize=14, fontweight='bold')
ax1.set_xlabel('Feature X')
ax1.set_ylabel('Feature Y')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper left')

# Right Plot: K-Medoids
ax2.scatter(X[:, 0], X[:, 1], c=kmedoids_labels, cmap='viridis', alpha=0.6, edgecolors='k')
ax2.scatter(kmedoids_centers[:, 0], kmedoids_centers[:, 1], c='cyan', marker='D', s=180, 
            label='Actual Medoids\n(Real Data Points)', edgecolors='black')
ax2.set_title('K-Medoids Clustering', fontsize=14, fontweight='bold')
ax2.set_xlabel('Feature X')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper left')

plt.tight_layout()

# 5. Save the plot as a PNG image for GitHub
plt.savefig('clustering_comparison.png', dpi=300, bbox_inches='tight')
print("Plot successfully saved as 'clustering_comparison.png'")

plt.show()
```
