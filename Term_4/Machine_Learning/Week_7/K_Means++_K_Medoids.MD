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

### Python Implementation Script

Run the following script to generate the synthetic data, perform the clustering, and automatically export the comparison image.

```python
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from sklearn.cluster import KMeans

# ==========================================
# 1. SETUP DATA AND PURE-NUMPY ALGORITHMS
# ==========================================

# Generate reproducible synthetic data with 3 groups + extreme outliers
np.random.seed(42)
group1 = np.random.normal(loc=[2.0, 2.0], scale=0.5, size=(50, 2))
group2 = np.random.normal(loc=[7.0, 8.0], scale=0.6, size=(50, 2))
group3 = np.random.normal(loc=[12.0, 3.0], scale=0.5, size=(45, 2))
outliers = np.array([[16.0, 2.0], [16.5, 2.5], [17.0, 1.5]])  
X = np.vstack([group1, group2, group3, outliers])
k = 3

def run_kmeans_steps(X, k, max_iter=10):
    """Executes K-Means++ and logs the history of each iteration step."""
    # Use sklearn's KMeans with k-means++ initialization to get initial centers
    km = KMeans(n_clusters=k, init='k-means++', max_iter=1, n_init=1, random_state=42)
    km.fit(X)
    centers = km.cluster_centers_
    
    history = []
    for _ in range(max_iter):
        # Assign steps
        distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
        labels = np.argmin(distances, axis=1)
        history.append((centers.copy(), labels.copy()))
        # Update steps (Virtual Averages)
        new_centers = np.array([X[labels == i].mean(axis=0) if len(X[labels == i]) > 0 else centers[i] for i in range(k)])
        if np.allclose(centers, new_centers):
            break
        centers = new_centers
    return history

def run_kmedoids_steps(X, k, max_iter=10):
    """Executes a custom K-Medoids PAM loop tracking every iteration step."""
    # Seed initial medoids safely from the data array
    initial_idx = np.random.RandomState(42).choice(len(X), k, replace=False)
    medoids = X[initial_idx].copy()
    
    history = []
    for _ in range(max_iter):
        # Assign steps based on closest medoid
        distances = np.linalg.norm(X[:, np.newaxis] - medoids, axis=2)
        labels = np.argmin(distances, axis=1)
        history.append((medoids.copy(), labels.copy()))
        
        # Update steps (Must swap to an actual data point that minimizes cluster cost)
        new_medoids = medoids.copy()
        for i in range(k):
            cluster_points = X[labels == i]
            if len(cluster_points) == 0:
                continue
            # Compute total distance from all points in cluster to every candidate point
            pairwise_dist = np.linalg.norm(cluster_points[:, np.newaxis] - cluster_points, axis=2)
            best_idx = np.argmin(pairwise_dist.sum(axis=1))
            new_medoids[i] = cluster_points[best_idx]
            
        if np.allclose(medoids, new_medoids):
            break
        medoids = new_medoids
    return history

# Run both tracking engines
kmeans_history = run_kmeans_steps(X, k)
kmedoids_history = run_kmedoids_steps(X, k)
max_frames = max(len(kmeans_history), len(kmedoids_history))

# ==========================================
# 2. PLOTTING AND ANIMATION ENGINE
# ==========================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

def update(frame):
    ax1.clear()
    ax2.clear()
    
    # --- Frame selection logic for K-Means ---
    km_frame = min(frame, len(kmeans_history) - 1)
    km_centers, km_labels = kmeans_history[km_frame]
    ax1.scatter(X[:, 0], X[:, 1], c=km_labels, cmap='viridis', alpha=0.6, edgecolors='k')
    ax1.scatter(km_centers[:, 0], km_centers[:, 1], c='red', marker='X', s=250, 
                label='Calculated Centroids\n(Virtual Average)', edgecolors='black', zorder=5)
    ax1.set_title(f'K-Means++ Clustering (Step {km_frame + 1})', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Feature X')
    ax1.set_ylabel('Feature Y')
    ax1.grid(True, linestyle='--', alpha=0.4)
    ax1.legend(loc='upper left')
    
    # --- Frame selection logic for K-Medoids ---
    kmed_frame = min(frame, len(kmedoids_history) - 1)
    kmed_centers, kmed_labels = kmedoids_history[kmed_frame]
    ax2.scatter(X[:, 0], X[:, 1], c=kmed_labels, cmap='viridis', alpha=0.6, edgecolors='k')
    ax2.scatter(kmed_centers[:, 0], kmed_centers[:, 1], c='cyan', marker='D', s=180, 
                label='Actual Medoids\n(Real Data Points)', edgecolors='black', zorder=5)
    ax2.set_title(f'K-Medoids Clustering (Step {kmed_frame + 1})', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Feature X')
    ax2.grid(True, linestyle='--', alpha=0.4)
    ax2.legend(loc='upper left')
    
    plt.tight_layout()

# Render convergence animation loop smoothly
ani = FuncAnimation(fig, update, frames=max_frames, interval=1000, repeat=True)

# Save the final resolved frame as a clean static PNG file for GitHub
update(max_frames - 1)
plt.savefig('clustering_comparison.png', dpi=300, bbox_inches='tight')
print("Saved final convergence frame asset to 'clustering_comparison.png'")

# Display visualization panel
plt.show()
```
