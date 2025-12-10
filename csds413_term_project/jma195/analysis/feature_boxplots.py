'''
Feature box plot visualization script.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    
    features = {
        'V': 'Vocabulary Richness',
        'S': 'Sentence Length',
        'W': 'Word Length',
        'F': 'Function Word Frequency',
        'C': 'Capitalization Abnormality'
    }
    
    sns.set_style("whitegrid")
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    axes = axes.flatten()
    
    colors = {'Human': 'steelblue', 'Bot': 'coral'}
    
    for i, (feature, feature_name) in enumerate(features.items()):
        ax = axes[i]
        
        data = df[[feature, 'label']].copy()
        data['label'] = data['label'].str.capitalize()
        
        sns.boxplot(x='label', y=feature, data=data, ax=ax, palette=colors)
        
        ax.set_xlabel('', fontsize=12)
        ax.set_ylabel(feature_name, fontsize=12, labelpad=10)
        ax.set_title(f'{feature_name} Comparison', fontsize=14, pad=10)
        ax.grid(True, alpha=0.3, axis='y')
    
    fig.delaxes(axes[5])
    
    plt.tight_layout()
    plt.savefig('../../figures/feature_boxplots.png', dpi=300, bbox_inches='tight')

if __name__ == "__main__": main()
