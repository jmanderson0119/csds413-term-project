"""
Bot Detection Classification with Permutation Testing

Trains classifiers on stylometric features and validates using permutation tests.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
print("Loading data...")
df = pd.read_csv('data/tweepfake_features.csv', sep=';')

# Prepare features and labels
features = ['V', 'S', 'W', 'F', 'C']
X = df[features].values
y = (df['label'] == 'bot').astype(int)  # 1 for bot, 0 for human

print(f"Dataset: {len(X)} samples")
print(f"Features: {features}")
print(f"Class distribution: {y.value_counts().to_dict()}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nTraining set: {len(X_train)} samples")
print(f"Test set: {len(X_test)} samples")

# Define classifiers
classifiers = {
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'SVM (Linear)': SVC(kernel='linear', random_state=42),
    'SVM (RBF)': SVC(kernel='rbf', random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

# Train and evaluate
print("\n" + "="*80)
print("CLASSIFICATION RESULTS")
print("="*80)

results = []

for name, clf in classifiers.items():
    print(f"\n{name}:")
    print("-" * 60)
    
    # Train
    clf.fit(X_train_scaled, y_train)
    
    # Predict
    y_pred = clf.predict(X_test_scaled)
    
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
    cv_scores = cross_val_score(clf, X_train_scaled, y_train, cv=5)
    print(f"  CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    
    results.append({
        'Classifier': name,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1': f1,
        'CV_Mean': cv_scores.mean(),
        'CV_Std': cv_scores.std()
    })

# Results table
results_df = pd.DataFrame(results)
print("\n" + "="*80)
print("SUMMARY TABLE")
print("="*80)
print(results_df.to_string(index=False))

# Permutation test for best classifier
print("\n" + "="*80)
print("PERMUTATION TEST (Statistical Validation)")
print("="*80)

best_clf_name = results_df.loc[results_df['Accuracy'].idxmax(), 'Classifier']
best_clf = classifiers[best_clf_name]

print(f"\nTesting: {best_clf_name}")
print("Running 1000 permutations...")

# Permutation test
n_permutations = 1000
permutation_scores = []

for i in range(n_permutations):
    # Shuffle labels
    y_train_permuted = np.random.permutation(y_train)
    
    # Train on permuted data
    clf_perm = type(best_clf)(**best_clf.get_params())
    clf_perm.fit(X_train_scaled, y_train_permuted)
    
    # Test on real test set
    score = clf_perm.score(X_test_scaled, y_test)
    permutation_scores.append(score)
    
    if (i + 1) % 100 == 0:
        print(f"  Completed {i + 1}/{n_permutations} permutations")

permutation_scores = np.array(permutation_scores)

# Calculate p-value
real_score = best_clf.score(X_test_scaled, y_test)
p_value = (permutation_scores >= real_score).sum() / n_permutations

print(f"\nReal model accuracy: {real_score:.4f}")
print(f"Mean permuted accuracy: {permutation_scores.mean():.4f}")
print(f"Std permuted accuracy: {permutation_scores.std():.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("✓ Model is significantly better than chance (p < 0.05)")
else:
    print("✗ Model is NOT significantly better than chance")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Permutation distribution
axes[0].hist(permutation_scores, bins=50, alpha=0.7, edgecolor='black')
axes[0].axvline(real_score, color='red', linestyle='--', linewidth=2, 
                label=f'Real Score: {real_score:.4f}')
axes[0].set_xlabel('Accuracy')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Permutation Test Distribution')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Confusion matrix
cm = confusion_matrix(y_test, best_clf.predict(X_test_scaled))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
            xticklabels=['Human', 'Bot'], yticklabels=['Human', 'Bot'])
axes[1].set_xlabel('Predicted')
axes[1].set_ylabel('Actual')
axes[1].set_title(f'Confusion Matrix - {best_clf_name}')

plt.tight_layout()
plt.savefig('visuals/classification_results.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'classification_results.png'")
plt.show()

# Feature importance (if Random Forest)
if 'Random Forest' in best_clf_name:
    importances = best_clf.feature_importances_
    feature_names = ['V', 'S', 'W', 'F', 'C']
    
    print("\n" + "="*80)
    print("FEATURE IMPORTANCE")
    print("="*80)
    for feat, imp in zip(feature_names, importances):
        print(f"  {feat}: {imp:.4f}")

# Save results
results_df.to_csv('results/classification_results.csv', index=False)
print("\n✓ Results saved to 'classification_results.csv'")

print("\n" + "="*80)
print("CLASSIFICATION COMPLETE")
print("="*80)
