import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
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

def run_kmeans_steps(X, k, max_iter=15):
    """Executes K-Means++ and logs the history of each iteration step."""
    km = KMeans(n_clusters=k, init='k-means++', max_iter=1, n_init=1, random_state=42)
    km.fit(X)
    centers = km.cluster_centers_
    
    history = []
    for _ in range(max_iter):
        distances = np.linalg.norm(X[:, np.newaxis] - centers, axis=2)
        labels = np.argmin(distances, axis=1)
        history.append((centers.copy(), labels.copy()))
        
        new_centers = np.array([X[labels == i].mean(axis=0) if len(X[labels == i]) > 0 else centers[i] for i in range(k)])
        if np.allclose(centers, new_centers):
            # Pad the final frame so the animation rests on convergence
            for _ in range(3): history.append((centers.copy(), labels.copy()))
            break
        centers = new_centers
    return history

def run_kmedoids_steps(X, k, max_iter=15):
    """Executes a custom K-Medoids PAM loop tracking every iteration step."""
    initial_idx = np.random.RandomState(42).choice(len(X), k, replace=False)
    medoids = X[initial_idx].copy()
    
    history = []
    for _ in range(max_iter):
        distances = np.linalg.norm(X[:, np.newaxis] - medoids, axis=2)
        labels = np.argmin(distances, axis=1)
        history.append((medoids.copy(), labels.copy()))
        
        new_medoids = medoids.copy()
        for i in range(k):
            cluster_points = X[labels == i]
            if len(cluster_points) == 0: continue
            pairwise_dist = np.linalg.norm(cluster_points[:, np.newaxis] - cluster_points, axis=2)
            best_idx = np.argmin(pairwise_dist.sum(axis=1))
            new_medoids[i] = cluster_points[best_idx]
            
        if np.allclose(medoids, new_medoids):
            # Pad the final frame so the animation rests on convergence
            for _ in range(3): history.append((medoids.copy(), labels.copy()))
            break
        medoids = new_medoids
    return history

# Run computational engines
kmeans_history = run_kmeans_steps(X, k)
kmedoids_history = run_kmedoids_steps(X, k)
max_frames = max(len(kmeans_history), len(kmedoids_history))

# ==========================================
# 2. ANIMATION AND EXPORT ENGINE
# ==========================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

def update(frame):
    ax1.clear()
    ax2.clear()
    
    # K-Means Frame Render
    km_frame = min(frame, len(kmeans_history) - 1)
    km_centers, km_labels = kmeans_history[km_frame]
    ax1.scatter(X[:, 0], X[:, 1], c=km_labels, cmap='viridis', alpha=0.6, edgecolors='k')
    ax1.scatter(km_centers[:, 0], km_centers[:, 1], c='red', marker='X', s=250, 
                label='Calculated Centroids\n(Virtual Average)', edgecolors='black', zorder=5)
    ax1.set_title(f'K-Means++ Convergence (Step {km_frame + 1})', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Feature X')
    ax1.set_ylabel('Feature Y')
    ax1.grid(True, linestyle='--', alpha=0.4)
    ax1.legend(loc='upper left')
    
    # K-Medoids Frame Render
    kmed_frame = min(frame, len(kmedoids_history) - 1)
    kmed_centers, kmed_labels = kmedoids_history[kmed_frame]
    ax2.scatter(X[:, 0], X[:, 1], c=kmed_labels, cmap='viridis', alpha=0.6, edgecolors='k')
    ax2.scatter(kmed_centers[:, 0], kmed_centers[:, 1], c='cyan', marker='D', s=180, 
                label='Actual Medoids\n(Real Data Points)', edgecolors='black', zorder=5)
    ax2.set_title(f'K-Medoids Convergence (Step {kmed_frame + 1})', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Feature X')
    ax2.grid(True, linestyle='--', alpha=0.4)
    ax2.legend(loc='upper left')
    
    plt.tight_layout()

# Initialize dynamic canvas
ani = FuncAnimation(fig, update, frames=max_frames, repeat=True)

# Save as a production-grade GIF using native Pillow compilation
print("Compiling animation frames into GIF file format... Please wait.")
writer = PillowWriter(fps=1.5)
ani.save('clustering_animation.gif', writer=writer, dpi=150)
print("File successfully built and saved as 'clustering_animation.gif'")

plt.show()
