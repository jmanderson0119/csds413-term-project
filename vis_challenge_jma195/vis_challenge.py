import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def mann_kendall_test(data):
    '''
    Performs Mann-Kendall trend test on time series graduation rates.
    
    :param data: Time series graduation rates
    :type data: array-like
    :returns: Tuple containing (S, p_value)
    :rtype: tuple
    '''
    n = len(data)
    
    # Calculates sum of signs of all pairwise differences
    # between every observation i to every later observation j
    S = 0
    for i in range(n-1):
        for j in range(i+1, n):
            S += np.sign(data[j] - data[i])

    # Calculates variance of S under H_0
    var_S = n * (n - 1) * (2 * n + 5) / 18
    
    # Calculates Z statistic for p-value computation
    if S > 0: Z = (S - 1) / np.sqrt(var_S)
    elif S < 0: Z = (S + 1) / np.sqrt(var_S)
    else: Z = 0
    
    # Computes p-value from standard normal distribution
    p_value = 2 * (1 - stats.norm.cdf(abs(Z)))
   
    return S, p_value

def plot_mann_kendall(grad_rates, results):
    '''
    Creates visualization of Mann-Kendall test results showing distribution 
    of pairwise comparisons for each category.
    
    :param grad_rates: Time series graduation rates
    :param results: Dictionary containing test results for each category
    :type results: dict
    '''
    fig, axes = plt.subplots(3, 1, figsize=(10, 14))

    fig.suptitle('Mann-Kendall Test: Distribution of Pairwise Comparisons', 
                 fontsize=18, fontweight='bold', y=0.98)

    plt.subplots_adjust(top=0.92, hspace=0.45)

    categories = ['Total', 'Men', 'Women']
    for i, category in enumerate(categories):
        ax = axes[i]
        
        # Computes all pairwise comparisons for current category
        n = len(grad_rates[category])
        concordant = 0
        discordant = 0
        all_comparisons = []
        
        for j in range(n-1):
            for k in range(j+1, n):
                diff = grad_rates[category].iloc[k] - grad_rates[category].iloc[j]
                all_comparisons.append(diff)
                if diff > 0: concordant += 1
                elif diff < 0: discordant += 1
        
        increases = [c for c in all_comparisons if c > 0]
        decreases = [c for c in all_comparisons if c < 0]
        zeros = [c for c in all_comparisons if c == 0]

        x_min = int(np.floor(min(all_comparisons)))
        x_max = int(np.ceil(max(all_comparisons)))
        bins = np.arange(x_min - 0.5, x_max + 1.5, 1)

        ax.hist(increases, bins=bins, alpha=0.7, color='green', 
                edgecolor='black', linewidth=0.5, label=f'Increases ({concordant})')
        ax.hist(decreases, bins=bins, alpha=0.7, color='red', 
                edgecolor='black', linewidth=0.5, label=f'Decreases ({discordant})')
        ax.hist(zeros, bins=bins, alpha=0.7, color='gray', 
                edgecolor='black', linewidth=0.5, label=f'No Change ({len(zeros)})')

        ax.axvline(0, color='black', linewidth=2, linestyle='--', alpha=0.5)

        ax.set_title(f"{category}\nS = {results[category]['S']}, p = {results[category]['p_value']:.4f}", 
                    fontsize=14, fontweight='bold')

        ax.set_xlabel('Change in Graduation Rate (%)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
        ax.legend(fontsize=10, loc='upper right')
        ax.grid(True, alpha=0.3, axis='y')

        ax.set_xticks(range(x_min, x_max + 1, 1))
        
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

    plt.savefig('mann_kendall.png', dpi=300, bbox_inches='tight')

def plot_enhanced_baseline(grad_rates, results):
    '''
    Creates enhanced baseline visualization with Mann-Kendall test results 
    overlaid on the graduation rate trends.
    
    :param grad_rates: Time series graduation rates
    :type grad_rates: pd.DataFrame
    :param results: Dictionary containing test results for each category
    :type results: dict
    '''
    _, ax = plt.subplots(figsize=(14, 8))
    
    y_min, y_max = 72, 93
    band_height = 2
    for i in range(int(y_min), int(y_max), band_height):
        if ((i - int(y_min)) // band_height) % 2 == 0:
            ax.axhspan(i, i + band_height, facecolor="#BCBBBB9D", alpha=0.5, zorder=0)
    
    colors = {'Total': '#5B9BD5', 'Men': '#70AD47', 'Women': '#ED7D31'}
    markers = {'Total': 's', 'Men': '^', 'Women': 'o'}
    
    categories = ['Total', 'Men', 'Women']
    for category in categories:
        ax.plot(grad_rates['Year_Numeric'], grad_rates[category], 
                marker=markers[category], markersize=6, linewidth=2.5,
                color=colors[category], label=category, alpha=0.8, zorder=3)
        
        # Calculates and plots sen's slope trend line
        x = grad_rates['Year_Numeric'].values
        y = grad_rates[category].values
        n = len(y)
        
        slopes = []
        for i in range(n-1):
            for j in range(i+1, n):
                slope = (y[j] - y[i]) / (x[j] - x[i])
                slopes.append(slope)
        sens_slope = np.median(slopes)
        
        median_i = n // 2
        median_x = x[median_i]
        median_y = y[median_i]
        trend_y = median_y + sens_slope * (x - median_x)
        
        ax.plot(x, trend_y, linestyle='--', linewidth=2, 
                color=colors[category], alpha=0.3, zorder=2,
                label=f'{category} Trend (slope={sens_slope:.2f}%/yr)')
        
        for i, (px, py) in enumerate(zip(grad_rates['Year_Numeric'], grad_rates[category])):
            ax.annotate(f'{py}%', xy=(px, py), xytext=(0, 9), textcoords='offset points',
                       ha='center', fontsize=8, fontweight='bold')
    
    stats_text = "Mann-Kendall Trend Test Results:\n"
    for category in categories:
        stats_text += f"{category}: S={results[category]['S']}, p={results[category]['p_value']:.4f}\n"
    
    ax.text(0.04, 0.96, stats_text.strip(), transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.8', facecolor='white', 
                                               edgecolor='gray', linewidth=1.5, alpha=0.95))
    
    ax.set_xlabel('Academic Year', fontsize=13, fontweight='bold')
    ax.set_ylabel('Graduation Rate (%)', fontsize=13, fontweight='bold')
    ax.set_title('Case Western Reserve University Graduation Rate Trends\n(2012-2024) with Statistical Validation', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(grad_rates['Year_Numeric'])
    ax.set_xticklabels([year.split('-')[0] for year in grad_rates['Year']], rotation=45, ha='right')
    
    ax.set_ylim([y_min, y_max])
    ax.set_yticks(range(y_min, y_max + 1, band_height))

    handles, labels = ax.get_legend_handles_labels()
    handles = [handles[i] for i in [0, 2, 4, 1, 3, 5]]
    labels = [labels[i] for i in [0, 2, 4, 1, 3, 5]]
    ax.legend(handles, labels, loc='lower right', fontsize=9, framealpha=0.9, ncol=2)    
    ax.grid(True, alpha=0.3, axis='y', zorder=1)
    ax.set_facecolor('white')
    
    plt.tight_layout()
    plt.savefig('enhanced_baseline.png', dpi=300, bbox_inches='tight')

def main():
    sns.set_theme(style="whitegrid", context="talk")
    sns.set_palette("husl")

    grad_rates = pd.read_csv("graduation_rates.csv")
    grad_rates['Year_Numeric'] = range(len(grad_rates))

    results = {}
    for category in ['Total', 'Men', 'Women']:
        S, p_value = mann_kendall_test(grad_rates[category].values)
        
        results[category] = {
            'S': S,
            'p_value': p_value,
        }

    plot_mann_kendall(grad_rates, results)
    plot_enhanced_baseline(grad_rates, results)

if __name__ == "__main__": main()
