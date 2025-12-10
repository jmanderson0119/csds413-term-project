"""
Author: Aishani Patil
Feature Engineering and Selection for Bot Detection

Analyzes quadratic and interaction features to identify the most useful ones
before adding them to the classification pipeline.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LassoCV
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations

# Load data
print("Loading data...")
df = pd.read_csv('data/tweepfake_features.csv', sep=';')

# Prepare features and labels
original_features = ['V', 'S', 'W', 'F', 'C']
X_original = df[original_features].values
y = (df['label'] == 'bot').astype(int)

print(f"Dataset: {len(X_original)} samples")
print(f"Original features: {original_features}")
print(f"Class distribution: {y.value_counts().to_dict()}")

# Split data
X_train_orig, X_test_orig, y_train, y_test = train_test_split(
    X_original, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize original features
scaler_orig = StandardScaler()
X_train_scaled = scaler_orig.fit_transform(X_train_orig)
X_test_scaled = scaler_orig.transform(X_test_orig)

print(f"\nTraining set: {len(X_train_scaled)} samples")
print(f"Test set: {len(X_test_scaled)} samples")

# Create polynomial features (degree 2 for quadratic and interactions)
print("\n" + "="*80)
print("GENERATING POLYNOMIAL FEATURES")
print("="*80)

poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Get feature names
feature_names = poly.get_feature_names_out(original_features)
print(f"Total features after polynomial expansion: {len(feature_names)}")

# Separate original, quadratic, and interaction features
original_indices = list(range(len(original_features)))
quadratic_indices = []
interaction_indices = []

for i, name in enumerate(feature_names):
    if '^2' in name:
        quadratic_indices.append(i)
    elif ' ' in name and '^2' not in name:
        interaction_indices.append(i)

print(f"Original features: {len(original_indices)}")
print(f"Quadratic features: {len(quadratic_indices)}")
print(f"Interaction features: {len(interaction_indices)}")

# Display new features
print(f"\nQuadratic features: {[feature_names[i] for i in quadratic_indices]}")
print(f"Interaction features: {[feature_names[i] for i in interaction_indices]}")

# Method 1: Statistical Feature Selection (F-score)
print("\n" + "="*80)
print("METHOD 1: STATISTICAL FEATURE SELECTION (F-SCORE)")
print("="*80)

f_scores, f_pvalues = f_classif(X_train_poly, y_train)

# Create feature analysis dataframe
feature_analysis = pd.DataFrame({
    'Feature': feature_names,
    'F_Score': f_scores,
    'P_Value': f_pvalues,
    'Type': ['Original'] * len(original_indices) + 
            ['Quadratic'] * len(quadratic_indices) + 
            ['Interaction'] * len(interaction_indices)
})

# Sort by F-score
feature_analysis = feature_analysis.sort_values('F_Score', ascending=False)
print("\nTop 15 features by F-score:")
print(feature_analysis.head(15).to_string(index=False))

# Method 2: Mutual Information
print("\n" + "="*80)
print("METHOD 2: MUTUAL INFORMATION")
print("="*80)

mi_scores = mutual_info_classif(X_train_poly, y_train, random_state=42)
feature_analysis['MI_Score'] = mi_scores

# Sort by mutual information
feature_analysis_mi = feature_analysis.sort_values('MI_Score', ascending=False)
print("\nTop 15 features by Mutual Information:")
print(feature_analysis_mi[['Feature', 'MI_Score', 'Type']].head(15).to_string(index=False))

# Method 3: Random Forest Feature Importance
print("\n" + "="*80)
print("METHOD 3: RANDOM FOREST FEATURE IMPORTANCE")
print("="*80)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_poly, y_train)
rf_importance = rf.feature_importances_

feature_analysis['RF_Importance'] = rf_importance
feature_analysis_rf = feature_analysis.sort_values('RF_Importance', ascending=False)
print("\nTop 15 features by Random Forest Importance:")
print(feature_analysis_rf[['Feature', 'RF_Importance', 'Type']].head(15).to_string(index=False))

# Method 4: LASSO Feature Selection
print("\n" + "="*80)
print("METHOD 4: LASSO REGULARIZATION")
print("="*80)

lasso = LassoCV(cv=5, random_state=42, max_iter=2000)
lasso.fit(X_train_poly, y_train)
lasso_coefs = np.abs(lasso.coef_)

feature_analysis['LASSO_Coef'] = lasso_coefs
feature_analysis_lasso = feature_analysis.sort_values('LASSO_Coef', ascending=False)

# Only show features with non-zero coefficients
non_zero_features = feature_analysis_lasso[feature_analysis_lasso['LASSO_Coef'] > 0]
print(f"\nLASSO selected {len(non_zero_features)} features:")
print(non_zero_features[['Feature', 'LASSO_Coef', 'Type']].to_string(index=False))

# Consensus Analysis
print("\n" + "="*80)
print("CONSENSUS ANALYSIS")
print("="*80)

# Normalize scores to 0-1 range for comparison
from sklearn.preprocessing import MinMaxScaler
scaler_scores = MinMaxScaler()

scores_matrix = np.column_stack([
    f_scores, mi_scores, rf_importance, lasso_coefs
])
scores_normalized = scaler_scores.fit_transform(scores_matrix)

feature_analysis['Consensus_Score'] = np.mean(scores_normalized, axis=1)
feature_analysis_consensus = feature_analysis.sort_values('Consensus_Score', ascending=False)

print("\nTop 15 features by consensus ranking:")
consensus_top = feature_analysis_consensus.head(15)
print(consensus_top[['Feature', 'Type', 'Consensus_Score', 'F_Score', 'MI_Score', 'RF_Importance', 'LASSO_Coef']].to_string(index=False))

# Analyze by feature type
print("\n" + "="*80)
print("ANALYSIS BY FEATURE TYPE")
print("="*80)

type_analysis = feature_analysis_consensus.groupby('Type').agg({
    'Consensus_Score': ['mean', 'std', 'count'],
    'F_Score': 'mean',
    'MI_Score': 'mean',
    'RF_Importance': 'mean'
}).round(4)

print("Average scores by feature type:")
print(type_analysis)

# Select best features from each category
print("\n" + "="*80)
print("RECOMMENDED FEATURES FOR CLASSIFICATION")
print("="*80)

# Get top features from each type
top_quadratic = feature_analysis_consensus[
    feature_analysis_consensus['Type'] == 'Quadratic'
].head(3)

top_interaction = feature_analysis_consensus[
    feature_analysis_consensus['Type'] == 'Interaction'
].head(5)

recommended_features = pd.concat([
    feature_analysis_consensus[feature_analysis_consensus['Type'] == 'Original'],
    top_quadratic,
    top_interaction
])

print("Recommended features to add:")
print(recommended_features[['Feature', 'Type', 'Consensus_Score']].to_string(index=False))

# Performance comparison
print("\n" + "="*80)
print("PERFORMANCE COMPARISON")
print("="*80)

# Baseline with original features
rf_baseline = RandomForestClassifier(n_estimators=100, random_state=42)
rf_baseline.fit(X_train_scaled, y_train)
baseline_score = rf_baseline.score(X_test_scaled, y_test)

# With top consensus features
top_k_indices = feature_analysis_consensus.head(10).index.tolist()
X_train_selected = X_train_poly[:, top_k_indices]
X_test_selected = X_test_poly[:, top_k_indices]

rf_enhanced = RandomForestClassifier(n_estimators=100, random_state=42)
rf_enhanced.fit(X_train_selected, y_train)
enhanced_score = rf_enhanced.score(X_test_selected, y_test)

print(f"Baseline accuracy (original features): {baseline_score:.4f}")
print(f"Enhanced accuracy (top 10 features): {enhanced_score:.4f}")
print(f"Improvement: {enhanced_score - baseline_score:.4f}")

# Visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Feature importance by type
type_scores = feature_analysis_consensus.groupby('Type')['Consensus_Score'].mean()
axes[0, 0].bar(type_scores.index, type_scores.values)
axes[0, 0].set_title('Average Consensus Score by Feature Type')
axes[0, 0].set_ylabel('Consensus Score')
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Top 15 features
top_15 = feature_analysis_consensus.head(15)
axes[0, 1].barh(range(len(top_15)), top_15['Consensus_Score'])
axes[0, 1].set_yticks(range(len(top_15)))
axes[0, 1].set_yticklabels(top_15['Feature'], fontsize=8)
axes[0, 1].set_title('Top 15 Features by Consensus Score')
axes[0, 1].set_xlabel('Consensus Score')

# 3. Correlation between different scoring methods
correlation_data = feature_analysis[['F_Score', 'MI_Score', 'RF_Importance', 'LASSO_Coef']].corr()
sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0, ax=axes[1, 0])
axes[1, 0].set_title('Correlation Between Scoring Methods')

# 4. Performance comparison
methods = ['Baseline\n(Original)', 'Enhanced\n(Top 10)']
scores = [baseline_score, enhanced_score]
bars = axes[1, 1].bar(methods, scores)
axes[1, 1].set_title('Performance Comparison')
axes[1, 1].set_ylabel('Accuracy')
axes[1, 1].set_ylim(0.5, 0.7)

# Add value labels on bars
for bar, score in zip(bars, scores):
    axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                   f'{score:.4f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('visuals/feature_engineering_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'feature_engineering_analysis.png'")
plt.show()

# Save results
feature_analysis_consensus.to_csv('results/feature_analysis.csv', index=False)
recommended_features.to_csv('results/recommended_features.csv', index=False)

# Create feature mapping for easy use in classification
selected_feature_names = recommended_features['Feature'].tolist()
selected_indices = [list(feature_names).index(name) for name in selected_feature_names]

feature_mapping = {
    'feature_names': selected_feature_names,
    'feature_indices': selected_indices,
    'polynomial_transformer': poly,
    'original_scaler': scaler_orig
}

# Save as numpy file for easy loading
np.save('results/feature_mapping.npy', feature_mapping)

print("\n✓ Feature analysis saved to 'feature_analysis.csv'")
print("✓ Recommended features saved to 'recommended_features.csv'")
print("✓ Feature mapping saved to 'feature_mapping.npy'")

print("\n" + "="*80)
print("FEATURE ENGINEERING ANALYSIS COMPLETE")
print("="*80)
print(f"\nSUMMARY:")
print(f"- Generated {len(feature_names)} total features from {len(original_features)} original")
print(f"- Recommended {len(recommended_features)} features for classification")
print(f"- Performance improvement: {enhanced_score - baseline_score:.4f}")
print(f"- Best quadratic features: {top_quadratic['Feature'].tolist()}")
print(f"- Best interaction features: {top_interaction['Feature'].tolist()}")