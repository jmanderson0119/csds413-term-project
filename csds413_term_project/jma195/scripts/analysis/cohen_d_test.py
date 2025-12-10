'''
Cohen's d effect size computation.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import numpy as np

def compute_cohens_d(group1: np.ndarray, group2: np.ndarray) -> float:
    '''
    Computes Cohen's d effect size between two groups.
    
    :param group1: Data for first group
    :type group1: np.ndarray
    :param group2: Data for second group
    :type group2: np.ndarray
    :returns: Cohen's d effect size
    :rtype: float
    '''
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    d = (np.mean(group1) - np.mean(group2)) / pooled_std
    
    return d

def main():
    np.random.seed(42)
    
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    
    human_data = df[df['label'] == 'human']
    bot_data = df[df['label'] == 'bot']
    
    features = ['V', 'S', 'W', 'F', 'C']
    print(f"{'Feature':<30} {'Human Mean':<12} {'Bot Mean':<12} {'Cohen\'s d':<12}")
    
    for feature in features:
        human_vals = human_data[feature].values
        bot_vals = bot_data[feature].values
        
        human_mean = np.mean(human_vals)
        bot_mean = np.mean(bot_vals)
        
        d = compute_cohens_d(human_vals, bot_vals)
        
        print(f"{feature:<30} {human_mean:<12.4f} {bot_mean:<12.4f} {d:<12.4f}")
        
if __name__ == "__main__": main()
