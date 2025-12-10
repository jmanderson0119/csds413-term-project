'''
KS test script.

:author: Jacob Anderson
:version: 0.1.0
'''

import pandas as pd
import numpy as np
from scipy import stats


def main():
    np.random.seed(42)
    df = pd.read_csv('../../data/tweepfake_features.csv', sep=';')
    
    results = []
    for feature in ['V', 'S', 'W', 'F', 'C']:
        human_data = df[df['label'] == 'human'][feature].values
        bot_data = df[df['label'] == 'bot'][feature].values
        
        ks_stat, p_value = stats.ks_2samp(human_data, bot_data)
        
        results.append({
            'feature': feature,
            'ks_statistic': ks_stat,
            'p_value': p_value
        })
    
    results_df = pd.DataFrame(results)
    
    print(results_df.to_string(index=False))

if __name__ == "__main__": main()
