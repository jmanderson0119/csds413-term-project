'''
Feature distribution visualization script for the extracted features.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_feature_distribution(features_df: pd.DataFrame, feature: str, 
                              feature_name: str, output_path: str):
    '''
    Plots the distribution of a single feature for human and bot tweets.
    
    :param features_df: DataFrame containing features and labels
    :type features_df: pd.DataFrame
    :param feature: Feature column name
    :type feature: str
    :param feature_name: Full descriptive name of the feature
    :type feature_name: str
    :param output_path: Path to save the figure
    :type output_path: str
    '''
    sns.set_style("whitegrid")
    sns.set_palette("muted")
    plt.figure(figsize=(10, 6))
    
    colors = {'human': 'steelblue', 'bot': 'coral'}
    
    for label in ['human', 'bot']:
        data = features_df[features_df['label'] == label][feature]
        plt.hist(data, bins=40, alpha=0.6, label=label.capitalize(), 
                color=colors[label], edgecolor='white', density=True)
    
    plt.xlabel(feature_name, fontsize=14, labelpad=15)
    plt.ylabel('Density', fontsize=14, labelpad=15)
    plt.title(f'{feature_name} Distribution', fontsize=16, pad=20)
    plt.legend(fontsize=12, loc='best')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

def main():
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    
    features = {
        'V': 'Vocabulary Richness',
        'S': 'Sentence Length',
        'W': 'Word Length',
        'F': 'Function Word Frequency',
        'C': 'Capitalization Abnormality'
    }
    
    for feature, feature_name in features.items():
        output_path = os.path.join('../../figures', f'{feature}_distribution.png')
        plot_feature_distribution(df, feature, feature_name, output_path)

if __name__ == "__main__": main()
