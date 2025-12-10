"""
Author: Aishani Patil
Enhanced Bot Detection Classification with Selected Polynomial Features

Uses the best quadratic and interaction features identified through feature selection.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

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
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_orig)
X_test_scaled = scaler.transform(X_test_orig)

# Create polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Get all feature names
all_feature_names = poly.get_feature_names_out(original_features)

# Select the best features based on our analysis
selected_features = [
    'V', 'S', 'W', 'F', 'C',  # Original features
    'V S', 'V^2', 'V F',       # Best quadratic features
    'W F', 'F^2', 'S W', 'W C', 'W^2'  # Best interaction features
]

# Get indices of selected features
selected_indices = [list(all_feature_names).index(feat) for feat in selected_features]

# Create feature sets for comparison
X_train_original = X_train_scaled
X_test_original = X_test_scaled

X_train_enhanced = X_train_poly[:, selected_indices]
X_test_enhanced = X_test_poly[:, selected_indices]

print(f"\nTraining set: {len(X_train_original)} samples")
print(f"Test set: {len(X_test_original)} samples")
print(f"Original features: {len(original_features)}")
print(f"Enhanced features: {len(selected_features)}")
print(f"Selected features: {selected_features}")

# Define classifiers
classifiers = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'SVM (Linear)': SVC(kernel='linear', random_state=42),
    'SVM (RBF)': SVC(kernel='rbf', random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Neural Network': MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, 
                                   random_state=42, early_stopping=True),
    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
    'Naive Bayes': GaussianNB(),
    'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5)
}

# Function to evaluate classifiers
def evaluate_classifiers(X_train, X_test, feature_set_name):
    print(f"\n{'='*80}")
    print(f"CLASSIFICATION RESULTS - {feature_set_name}")
    print(f"{'='*80}")
    
    results = []
    
    for name, clf in classifiers.items():
        print(f"\n{name}:")
        print("-" * 60)
        
        # Train
        clf.fit(X_train, y_train)
        
        # Predict
        y_pred = clf.predict(X_test)
        
        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision, recall, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average='binary'
        )
        
        print(f"  Accuracy:  {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall:    {recall:.4f}")
        print(f"  F1-Score:  {f1:.4f}")
        
        # Cross-validation
        cv_scores = cross_val_score(clf, X_train, y_train, cv=5)
        print(f"  CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        results.append({
            'Classifier': name,
            'Feature_Set': feature_set_name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1': f1,
            'CV_Mean': cv_scores.mean(),
            'CV_Std': cv_scores.std()
        })
    
    return results

# Evaluate both feature sets
original_results = evaluate_classifiers(X_train_original, X_test_original, "Original Features")
enhanced_results = evaluate_classifiers(X_train_enhanced, X_test_enhanced, "Enhanced Features")

# Combine results
all_results = original_results + enhanced_results
results_df = pd.DataFrame(all_results)

# Comparison analysis
print(f"\n{'='*80}")
print("FEATURE SET COMPARISON")
print(f"{'='*80}")

comparison = results_df.pivot_table(
    index='Classifier', 
    columns='Feature_Set', 
    values=['Accuracy', 'F1'], 
    aggfunc='mean'
)

print("\nAccuracy Comparison:")
accuracy_comp = comparison['Accuracy']
accuracy_comp['Improvement'] = accuracy_comp['Enhanced Features'] - accuracy_comp['Original Features']
print(accuracy_comp.round(4))

print("\nF1-Score Comparison:")
f1_comp = comparison['F1']
f1_comp['Improvement'] = f1_comp['Enhanced Features'] - f1_comp['Original Features']
print(f1_comp.round(4))

# Best performing models
print(f"\n{'='*80}")
print("BEST PERFORMING MODELS")
print(f"{'='*80}")

best_original = results_df[results_df['Feature_Set'] == 'Original Features'].loc[
    results_df[results_df['Feature_Set'] == 'Original Features']['Accuracy'].idxmax()
]

best_enhanced = results_df[results_df['Feature_Set'] == 'Enhanced Features'].loc[
    results_df[results_df['Feature_Set'] == 'Enhanced Features']['Accuracy'].idxmax()
]

print(f"Best Original: {best_original['Classifier']} - Accuracy: {best_original['Accuracy']:.4f}")
print(f"Best Enhanced: {best_enhanced['Classifier']} - Accuracy: {best_enhanced['Accuracy']:.4f}")
print(f"Overall Improvement: {best_enhanced['Accuracy'] - best_original['Accuracy']:.4f}")

# Feature importance analysis for best enhanced model
best_enhanced_clf_name = best_enhanced['Classifier']
if any(model_type in best_enhanced_clf_name for model_type in ['Random Forest', 'Gradient Boosting']):
    print(f"\n{'='*80}")
    print(f"FEATURE IMPORTANCE - {best_enhanced_clf_name}")
    print(f"{'='*80}")
    
    # Retrain the best model to get feature importance
    best_clf = classifiers[best_enhanced_clf_name]
    best_clf.fit(X_train_enhanced, y_train)
    
    importances = best_clf.feature_importances_
    feature_importance_df = pd.DataFrame({
        'Feature': selected_features,
        'Importance': importances,
        'Type': ['Original']*5 + ['Quadratic']*3 + ['Interaction']*5
    }).sort_values('Importance', ascending=False)
    
    print(feature_importance_df.to_string(index=False))

# Visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Accuracy comparison
accuracy_data = results_df.pivot(index='Classifier', columns='Feature_Set', values='Accuracy')
accuracy_data.plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Accuracy Comparison by Feature Set')
axes[0, 0].set_ylabel('Accuracy')
axes[0, 0].legend(title='Feature Set')
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. F1-Score comparison
f1_data = results_df.pivot(index='Classifier', columns='Feature_Set', values='F1')
f1_data.plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('F1-Score Comparison by Feature Set')
axes[0, 1].set_ylabel('F1-Score')
axes[0, 1].legend(title='Feature Set')
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Improvement heatmap
improvement_data = pd.DataFrame({
    'Accuracy_Improvement': accuracy_comp['Improvement'],
    'F1_Improvement': f1_comp['Improvement']
})
sns.heatmap(improvement_data.T, annot=True, cmap='RdYlGn', center=0, ax=axes[1, 0])
axes[1, 0].set_title('Performance Improvement with Enhanced Features')
axes[1, 0].set_xlabel('Classifier')

# 4. Feature importance (if available)
if any(model_type in best_enhanced_clf_name for model_type in ['Random Forest', 'Gradient Boosting']):
    feature_importance_df.set_index('Feature')['Importance'].plot(kind='barh', ax=axes[1, 1])
    axes[1, 1].set_title(f'Feature Importance - {best_enhanced_clf_name}')
    axes[1, 1].set_xlabel('Importance')
else:
    # Show feature type distribution instead
    type_counts = pd.Series(['Original']*5 + ['Quadratic']*3 + ['Interaction']*5).value_counts()
    type_counts.plot(kind='pie', ax=axes[1, 1], autopct='%1.1f%%')
    axes[1, 1].set_title('Selected Feature Type Distribution')

plt.tight_layout()
plt.savefig('visuals/enhanced_classification_results.png', dpi=300, bbox_inches='tight')
print(f"\n✓ Visualization saved as 'enhanced_classification_results.png'")
plt.show()

# Permutation test for best enhanced model
print(f"\n{'='*80}")
print("PERMUTATION TEST - BEST ENHANCED MODEL")
print(f"{'='*80}")

best_clf = classifiers[best_enhanced_clf_name]
best_clf.fit(X_train_enhanced, y_train)

print(f"Testing: {best_enhanced_clf_name} with Enhanced Features")
print("Running 1000 permutations...")

n_permutations = 1000
permutation_scores = []

for i in range(n_permutations):
    y_train_permuted = np.random.permutation(y_train)
    clf_perm = type(best_clf)(**best_clf.get_params())
    clf_perm.fit(X_train_enhanced, y_train_permuted)
    score = clf_perm.score(X_test_enhanced, y_test)
    permutation_scores.append(score)
    
    if (i + 1) % 200 == 0:
        print(f"  Completed {i + 1}/{n_permutations} permutations")

permutation_scores = np.array(permutation_scores)
real_score = best_clf.score(X_test_enhanced, y_test)
p_value = (permutation_scores >= real_score).sum() / n_permutations

print(f"\nReal model accuracy: {real_score:.4f}")
print(f"Mean permuted accuracy: {permutation_scores.mean():.4f}")
print(f"Std permuted accuracy: {permutation_scores.std():.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("✓ Enhanced model is significantly better than chance (p < 0.05)")
else:
    print("✗ Enhanced model is NOT significantly better than chance")

# Save results
results_df.to_csv('results/enhanced_classification_results.csv', index=False)
comparison.to_csv('results/feature_set_comparison.csv')

print(f"\n✓ Results saved to 'enhanced_classification_results.csv'")
print(f"✓ Comparison saved to 'feature_set_comparison.csv'")

print(f"\n{'='*80}")
print("ENHANCED CLASSIFICATION COMPLETE")
print(f"{'='*80}")

# Summary
print(f"\nSUMMARY:")
print(f"- Added {len(selected_features) - len(original_features)} polynomial features")
print(f"- Best original model: {best_original['Classifier']} ({best_original['Accuracy']:.4f})")
print(f"- Best enhanced model: {best_enhanced['Classifier']} ({best_enhanced['Accuracy']:.4f})")
print(f"- Performance change: {best_enhanced['Accuracy'] - best_original['Accuracy']:.4f}")

# Count improvements
improvements = (accuracy_comp['Improvement'] > 0).sum()
total_models = len(accuracy_comp)
print(f"- Models improved: {improvements}/{total_models}")
print(f"- Average accuracy improvement: {accuracy_comp['Improvement'].mean():.4f}")