'''
PCA visualization script.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def main():
    np.random.seed(42)
    
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    feature_cols = ['V', 'S', 'W', 'F', 'C']
    
    scaler = StandardScaler()
    features_standardized = scaler.fit_transform(df[feature_cols])
    
    pca = PCA(n_components=2)
    pca_coords = pca.fit_transform(features_standardized)
    
    df['PC1'] = pca_coords[:, 0]
    df['PC2'] = pca_coords[:, 1]
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 8))
    
    colors = {'human': 'steelblue', 'bot': 'coral'}
    
    for label in ['human', 'bot']:
        subset = df[df['label'] == label]
        plt.scatter(subset['PC1'], subset['PC2'], 
                   c=colors[label], label=label.capitalize(),
                   alpha=0.4, s=20, edgecolors='none')
    
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)', 
              fontsize=14, labelpad=15)
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)', 
              fontsize=14, labelpad=15)
    plt.title('PCA Projection of Tweet Features', fontsize=16, pad=20)
    plt.legend(fontsize=12, loc='best')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../../figures/pca_projection.png', dpi=300, bbox_inches='tight')

if __name__ == "__main__": main()
