'''
Feature contribution analysis script.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def compute_pooled_covariance(data_human: np.ndarray, 
                              data_bot: np.ndarray) -> np.ndarray:
    '''
    Computes pooled covariance matrix for two groups.
    
    :param data_human: Feature matrix for human tweets
    :type data_human: np.ndarray
    :param data_bot: Feature matrix for bot tweets
    :type data_bot: np.ndarray
    :returns: Pooled covariance matrix
    :rtype: np.ndarray
    '''
    n_human = data_human.shape[0]
    n_bot = data_bot.shape[0]
    
    cov_human = np.cov(data_human, rowvar=False)
    cov_bot = np.cov(data_bot, rowvar=False)
    
    pooled_cov = ((n_human - 1) * cov_human + (n_bot - 1) * cov_bot) / \
                 (n_human + n_bot - 2)
    
    return pooled_cov

def main():
    np.random.seed(42)
    
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    feature_cols = ['V', 'S', 'W', 'F', 'C']
    
    scaler = StandardScaler()
    features_standardized = scaler.fit_transform(df[feature_cols])
    
    df_scaled = df.copy()
    df_scaled[feature_cols] = features_standardized
    
    human_data = df_scaled[df_scaled['label'] == 'human'][feature_cols].values
    bot_data = df_scaled[df_scaled['label'] == 'bot'][feature_cols].values
    
    mean_diff = human_data.mean(axis=0) - bot_data.mean(axis=0)
    pooled_cov = compute_pooled_covariance(human_data, bot_data)
    cov_inv = np.linalg.inv(pooled_cov)
    
    contributions = mean_diff * (cov_inv @ mean_diff)
    total = contributions.sum()
    
    print("Feature Contributions to Mahalanobis Distance:")
    print()
    for name, contrib in zip(feature_cols, contributions):
        pct = (contrib / total) * 100
        print(f"{name}: {contrib:.4f} ({pct:.1f}%)")
    print()
    print(f"Total: {total:.4f}")
    print()
    print(f"Covariance matrix condition number: {np.linalg.cond(pooled_cov):.2f}")

if __name__ == "__main__": main()
