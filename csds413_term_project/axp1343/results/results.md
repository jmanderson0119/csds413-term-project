(my_env) aishanipatil@Aishanis-MacBook-Pro-5 csds413_term_project % python3 scripts/classification.py
Loading data...
Dataset: 22930 samples
Features: ['V', 'S', 'W', 'F', 'C']
Class distribution: {0: 11602, 1: 11328}

Training set: 18344 samples
Test set: 4586 samples

================================================================================
CLASSIFICATION RESULTS
================================================================================

Logistic Regression:
------------------------------------------------------------
  Accuracy:  0.5689
  Precision: 0.5632
  Recall:    0.5680
  F1-Score:  0.5656
  CV Accuracy: 0.5817 (+/- 0.0104)

SVM (Linear):
------------------------------------------------------------
  Accuracy:  0.5787
  Precision: 0.5727
  Recall:    0.5803
  F1-Score:  0.5765
  CV Accuracy: 0.5864 (+/- 0.0075)

SVM (RBF):
------------------------------------------------------------
  Accuracy:  0.6223
  Precision: 0.6217
  Recall:    0.6019
  F1-Score:  0.6117
  CV Accuracy: 0.6121 (+/- 0.0073)

Random Forest:
------------------------------------------------------------
  Accuracy:  0.6053
  Precision: 0.6036
  Recall:    0.5861
  F1-Score:  0.5947
  CV Accuracy: 0.6046 (+/- 0.0087)

================================================================================
SUMMARY TABLE
================================================================================
         Classifier  Accuracy  Precision   Recall       F1  CV_Mean   CV_Std
Logistic Regression  0.568905   0.563239 0.567961 0.565590 0.581662 0.010381
       SVM (Linear)  0.578718   0.572735 0.580318 0.576502 0.586404 0.007547
          SVM (RBF)  0.622329   0.621696 0.601942 0.611659 0.612135 0.007263
      Random Forest  0.605321   0.603636 0.586055 0.594716 0.604557 0.008717

================================================================================
PERMUTATION TEST (Statistical Validation)
================================================================================

Testing: SVM (RBF)
Running 1000 permutations...
  Completed 100/1000 permutations
  Completed 200/1000 permutations
  Completed 300/1000 permutations
  Completed 400/1000 permutations
  Completed 500/1000 permutations
  Completed 600/1000 permutations
  Completed 700/1000 permutations
  Completed 800/1000 permutations
  Completed 900/1000 permutations
  Completed 1000/1000 permutations

Real model accuracy: 0.6223
Mean permuted accuracy: 0.5048
Std permuted accuracy: 0.0254
p-value: 0.0000
✓ Model is significantly better than chance (p < 0.05)

✓ Visualization saved as 'classification_results.png'

✓ Results saved to 'classification_results.csv'

================================================================================
CLASSIFICATION COMPLETE
================================================================================
(my_env) aishanipatil@Aishanis-MacBook-Pro-5 csds413_term_project % 