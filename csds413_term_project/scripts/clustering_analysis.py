"""
Author: Aishani Patil
Clustering Analysis with t-SNE and PCA Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Load data
print("Loading data...")
df = pd.read_csv('data/tweepfake_features.csv', sep=';')

features = ['V', 'S', 'W', 'F', 'C']
X = df[features].values
labels = df['label'].values  # True labels (bot/human)

print(f"Dataset: {len(X)} samples")
print(f"Features: {features}")

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================================================
# K-MEANS CLUSTERING
# ============================================================================
print("\n" + "="*80)
print("K-MEANS CLUSTERING")
print("="*80)

kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_scaled)

# Compare clusters to true labels
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

ari = adjusted_rand_score(labels, cluster_labels)
nmi = normalized_mutual_info_score(labels, cluster_labels)

print(f"\nAdjusted Rand Index: {ari:.4f}")
print(f"Normalized Mutual Information: {nmi:.4f}")
print(f"\nCluster 0: {(cluster_labels == 0).sum()} samples")
print(f"Cluster 1: {(cluster_labels == 1).sum()} samples")

# ============================================================================
# PCA - 2D VISUALIZATION
# ============================================================================
print("\n" + "="*80)
print("PCA - 2D PROJECTION")
print("="*80)

pca_2d = PCA(n_components=2, random_state=42)
X_pca_2d = pca_2d.fit_transform(X_scaled)

print(f"Explained variance: {pca_2d.explained_variance_ratio_}")
print(f"Total variance explained: {pca_2d.explained_variance_ratio_.sum():.4f}")

# ============================================================================
# PCA - 3D VISUALIZATION
# ============================================================================
print("\n" + "="*80)
print("PCA - 3D PROJECTION")
print("="*80)

pca_3d = PCA(n_components=3, random_state=42)
X_pca_3d = pca_3d.fit_transform(X_scaled)

print(f"Explained variance: {pca_3d.explained_variance_ratio_}")
print(f"Total variance explained: {pca_3d.explained_variance_ratio_.sum():.4f}")

# ============================================================================
# t-SNE - 2D VISUALIZATION
# ============================================================================
print("\n" + "="*80)
print("t-SNE - 2D PROJECTION")
print("="*80)
print("Computing t-SNE (this may take a minute)...")

tsne_2d = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne_2d = tsne_2d.fit_transform(X_scaled)

print("✓ t-SNE 2D complete")

# ============================================================================
# t-SNE - 3D VISUALIZATION
# ============================================================================
print("\n" + "="*80)
print("t-SNE - 3D PROJECTION")
print("="*80)
print("Computing t-SNE 3D (this may take a minute)...")

tsne_3d = TSNE(n_components=3, random_state=42, perplexity=30)
X_tsne_3d = tsne_3d.fit_transform(X_scaled)

print("✓ t-SNE 3D complete")

# ============================================================================
# VISUALIZATION - 2D PLOTS
# ============================================================================
print("\n" + "="*80)
print("CREATING 2D VISUALIZATIONS")
print("="*80)

fig, axes = plt.subplots(2, 2, figsize=(16, 14))

# Color mapping
colors = {'bot': 'red', 'human': 'blue'}
label_colors = [colors[label] for label in labels]

# PCA 2D - True Labels
axes[0, 0].scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=label_colors, 
                   alpha=0.6, s=20, edgecolors='black', linewidth=0.5)
axes[0, 0].set_xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]:.2%})')
axes[0, 0].set_ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]:.2%})')
axes[0, 0].set_title('PCA 2D - True Labels', fontsize=14, fontweight='bold')
axes[0, 0].legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
               markersize=10, label='Bot'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
               markersize=10, label='Human')
])
axes[0, 0].grid(True, alpha=0.3)

# PCA 2D - K-Means Clusters
cluster_colors = ['orange' if c == 0 else 'green' for c in cluster_labels]
axes[0, 1].scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=cluster_colors, 
                   alpha=0.6, s=20, edgecolors='black', linewidth=0.5)
axes[0, 1].set_xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]:.2%})')
axes[0, 1].set_ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]:.2%})')
axes[0, 1].set_title('PCA 2D - K-Means Clusters', fontsize=14, fontweight='bold')
axes[0, 1].legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', 
               markersize=10, label='Cluster 0'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', 
               markersize=10, label='Cluster 1')
])
axes[0, 1].grid(True, alpha=0.3)

# t-SNE 2D - True Labels
axes[1, 0].scatter(X_tsne_2d[:, 0], X_tsne_2d[:, 1], c=label_colors, 
                   alpha=0.6, s=20, edgecolors='black', linewidth=0.5)
axes[1, 0].set_xlabel('t-SNE Dimension 1')
axes[1, 0].set_ylabel('t-SNE Dimension 2')
axes[1, 0].set_title('t-SNE 2D - True Labels', fontsize=14, fontweight='bold')
axes[1, 0].legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
               markersize=10, label='Bot'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
               markersize=10, label='Human')
])
axes[1, 0].grid(True, alpha=0.3)

# t-SNE 2D - K-Means Clusters
axes[1, 1].scatter(X_tsne_2d[:, 0], X_tsne_2d[:, 1], c=cluster_colors, 
                   alpha=0.6, s=20, edgecolors='black', linewidth=0.5)
axes[1, 1].set_xlabel('t-SNE Dimension 1')
axes[1, 1].set_ylabel('t-SNE Dimension 2')
axes[1, 1].set_title('t-SNE 2D - K-Means Clusters', fontsize=14, fontweight='bold')
axes[1, 1].legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', 
               markersize=10, label='Cluster 0'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', 
               markersize=10, label='Cluster 1')
])
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('visuals/clustering_2d.png', dpi=300, bbox_inches='tight')
print("✓ 2D visualizations saved as 'clustering_2d.png'")
plt.show()

# ============================================================================
# VISUALIZATION - 3D PLOTS
# ============================================================================
print("\n" + "="*80)
print("CREATING 3D VISUALIZATIONS")
print("="*80)

fig = plt.figure(figsize=(18, 8))

# PCA 3D - True Labels
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], 
            c=label_colors, alpha=0.6, s=20, edgecolors='black', linewidth=0.5)
ax1.set_xlabel(f'PC1 ({pca_3d.explained_variance_ratio_[0]:.2%})')
ax1.set_ylabel(f'PC2 ({pca_3d.explained_variance_ratio_[1]:.2%})')
ax1.set_zlabel(f'PC3 ({pca_3d.explained_variance_ratio_[2]:.2%})')
ax1.set_title('PCA 3D - True Labels', fontsize=14, fontweight='bold')
ax1.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
               markersize=10, label='Bot'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
               markersize=10, label='Human')
])

# t-SNE 3D - True Labels
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(X_tsne_3d[:, 0], X_tsne_3d[:, 1], X_tsne_3d[:, 2], 
            c=label_colors, alpha=0.6, s=20, edgecolors='black', linewidth=0.5)
ax2.set_xlabel('t-SNE Dimension 1')
ax2.set_ylabel('t-SNE Dimension 2')
ax2.set_zlabel('t-SNE Dimension 3')
ax2.set_title('t-SNE 3D - True Labels', fontsize=14, fontweight='bold')
ax2.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
               markersize=10, label='Bot'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
               markersize=10, label='Human')
])

plt.tight_layout()
plt.savefig('visuals/clustering_3d.png', dpi=300, bbox_inches='tight')
print("✓ 3D visualizations saved as 'clustering_3d.png'")
plt.show()

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "="*80)
print("CLUSTERING ANALYSIS COMPLETE")
print("="*80)
print(f"\nK-Means Clustering:")
print(f"  Adjusted Rand Index: {ari:.4f}")
print(f"  Normalized Mutual Info: {nmi:.4f}")
print(f"\nPCA:")
print(f"  2D variance explained: {pca_2d.explained_variance_ratio_.sum():.4f}")
print(f"  3D variance explained: {pca_3d.explained_variance_ratio_.sum():.4f}")
print(f"\nFiles saved:")
print(f"  - clustering_2d.png (4 subplots)")
print(f"  - clustering_3d.png (2 3D plots)")