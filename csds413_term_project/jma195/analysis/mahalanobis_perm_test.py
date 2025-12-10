'''
Mahalanobis distance permutation test script for TweepFake dataset.

:author: Jacob Anderson
:version: 0.1.0
'''

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

def compute_mahalanobis_distance(mean_human: np.ndarray, mean_bot: np.ndarray,
                                 cov_inv: np.ndarray) -> float:
    '''
    Computes Mahalanobis distance between two group centroids.
    
    :param mean_human: Mean feature vector for human tweets
    :type mean_human: np.ndarray
    :param mean_bot: Mean feature vector for bot tweets
    :type mean_bot: np.ndarray
    :param cov_inv: Inverse of pooled covariance matrix
    :type cov_inv: np.ndarray
    :returns: Mahalanobis distance
    :rtype: float
    '''
    diff = mean_human - mean_bot
    distance = np.sqrt(diff.T @ cov_inv @ diff)
    return distance

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

def mahalanobis_permutation_test(features_df: pd.DataFrame, 
                                 feature_cols: list,
                                 n_permutations: int = 10000) -> tuple:
    '''
    Performs permutation test using Mahalanobis distance as test statistic.
    
    :param features_df: DataFrame containing features and labels
    :type features_df: pd.DataFrame
    :param feature_cols: List of feature column names
    :type feature_cols: list
    :param n_permutations: Number of permutations
    :type n_permutations: int
    :returns: Tuple observed distance, p-value, null distribution
    :rtype: tuple
    '''
    
    scaler = StandardScaler()
    features_standardized = scaler.fit_transform(features_df[feature_cols])
    
    df_scaled = features_df.copy()
    df_scaled[feature_cols] = features_standardized
    
    human_data = df_scaled[df_scaled['label'] == 'human'][feature_cols].values
    bot_data = df_scaled[df_scaled['label'] == 'bot'][feature_cols].values
    
    mean_human_obs = human_data.mean(axis=0)
    mean_bot_obs = bot_data.mean(axis=0)
    
    pooled_cov = compute_pooled_covariance(human_data, bot_data)
    cov_inv = np.linalg.inv(pooled_cov)
    
    d_obs = compute_mahalanobis_distance(mean_human_obs, mean_bot_obs, cov_inv)
    
    combined_data = np.vstack([human_data, bot_data])
    labels = np.array(['human'] * len(human_data) + ['bot'] * len(bot_data))
    
    null_distribution = np.zeros(n_permutations)
    
    for i in range(n_permutations):
        permuted_labels = np.random.permutation(labels)
        
        perm_human_data = combined_data[permuted_labels == 'human']
        perm_bot_data = combined_data[permuted_labels == 'bot']
        
        mean_human_perm = perm_human_data.mean(axis=0)
        mean_bot_perm = perm_bot_data.mean(axis=0)
        
        d_perm = compute_mahalanobis_distance(mean_human_perm, mean_bot_perm, cov_inv)
        null_distribution[i] = d_perm
    
    p_value = (np.sum(null_distribution >= d_obs) + 1) / (n_permutations + 1)
    
    return d_obs, p_value, null_distribution

def plot_permutation_results(d_obs: float, null_distribution: np.ndarray,
                             p_value: float, output_path: str):
    '''
    Plots permutation test results with null distribution.
    
    :param d_obs: Observed Mahalanobis distance
    :type d_obs: float
    :param null_distribution: Array of permuted distances
    :type null_distribution: np.ndarray
    :param p_value: Computed p-value
    :type p_value: float
    :param output_path: Path to save the figure
    :type output_path: str
    '''
    sns.set_style("whitegrid")
    sns.set_palette("muted")
    plt.figure(figsize=(12, 7))
    
    plt.hist(null_distribution, bins=50, color='steelblue', alpha=0.7,
            edgecolor='white', density=False, label='Null Distribution')
    
    plt.axvline(d_obs, color='red', linestyle='--', linewidth=2.5,
               label=f'Observed Distance = {d_obs:.4f}')
    
    current_xlim = plt.xlim()
    plt.xlim(current_xlim[0], d_obs * 1.1)
    
    plt.text(0.90, 0.95, f'p-value = {p_value:.4f}',
            transform=plt.gca().transAxes,
            verticalalignment='top',
            horizontalalignment='right',
            fontsize=13,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.xlabel('Mahalanobis Distance', fontsize=14, labelpad=15)
    plt.ylabel('Frequency', fontsize=14, labelpad=15)
    plt.title('Mahalanobis Distance Permutation Test', fontsize=16, pad=20)
    
    plt.legend(fontsize=12, loc='upper center')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

def main():    
    parser = argparse.ArgumentParser(description='Mahalanobis distance permutation test')
    parser.add_argument('--features', type=str, default='V,S,W,F,C',
                       help='Comma-separated feature list')
    args = parser.parse_args()
    
    np.random.seed(42)
    
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    
    feature_cols = [f.strip() for f in args.features.split(',')]
    
    d_obs, p_value, null_dist = mahalanobis_permutation_test(df, feature_cols, n_permutations=10000)
    
    feature_string = ''.join(feature_cols)
    
    plot_permutation_results(d_obs, null_dist, p_value, f'../../figures/mahalanobis_test_{feature_string}.png')

if __name__ == "__main__": main()
