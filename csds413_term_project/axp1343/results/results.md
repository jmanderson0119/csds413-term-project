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




-----








(new_env) aishanipatil@Aishanis-MacBook-Pro-5 axp1343 % source new_env/bin/activate && python scripts/classification.py
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

Neural Network:
------------------------------------------------------------
  Accuracy:  0.6236
  Precision: 0.6069
  Recall:    0.6765
  F1-Score:  0.6398
  CV Accuracy: 0.6082 (+/- 0.0067)

Gradient Boosting:
------------------------------------------------------------
  Accuracy:  0.6188
  Precision: 0.6147
  Recall:    0.6125
  F1-Score:  0.6136
  CV Accuracy: 0.6124 (+/- 0.0104)

Naive Bayes:
------------------------------------------------------------
  Accuracy:  0.5587
  Precision: 0.5383
  Recall:    0.7502
  F1-Score:  0.6268
  CV Accuracy: 0.5573 (+/- 0.0084)

K-Nearest Neighbors:
------------------------------------------------------------
  Accuracy:  0.5887
  Precision: 0.5867
  Recall:    0.5675
  F1-Score:  0.5769
  CV Accuracy: 0.5927 (+/- 0.0060)

================================================================================
SUMMARY TABLE
================================================================================
         Classifier  Accuracy  Precision   Recall       F1  CV_Mean   CV_Std
Logistic Regression  0.568905   0.563239 0.567961 0.565590 0.581662 0.010381
       SVM (Linear)  0.578718   0.572735 0.580318 0.576502 0.586404 0.007547
          SVM (RBF)  0.622329   0.621696 0.601942 0.611659 0.612135 0.007263
      Random Forest  0.605321   0.603636 0.586055 0.594716 0.604557 0.008717
     Neural Network  0.623637   0.606888 0.676523 0.639816 0.608156 0.006738
  Gradient Boosting  0.618840   0.614703 0.612533 0.613616 0.612353 0.010368
        Naive Bayes  0.558657   0.538315 0.750221 0.626844 0.557349 0.008414
K-Nearest Neighbors  0.588748   0.586679 0.567520 0.576940 0.592673 0.006038

================================================================================
PERMUTATION TEST (Statistical Validation)
================================================================================

Testing: Neural Network
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

Real model accuracy: 0.6236
Mean permuted accuracy: 0.5052
Std permuted accuracy: 0.0284
p-value: 0.0000
✓ Model is significantly better than chance (p < 0.05)

✓ Visualization saved as 'classification_results.png'

✓ Results saved to 'classification_results.csv'

================================================================================
CLASSIFICATION COMPLETE
================================================================================




-----








after removing outliers


(new_env) aishanipatil@Aishanis-MacBook-Pro-5 axp1343 % source new_env/bin/activate && python scripts/classification.py
Loading data...
Dataset: 22137 samples
Features: ['V', 'S', 'W', 'F', 'C']
Class distribution: {1: 11164, 0: 10973}

Training set: 17709 samples
Test set: 4428 samples

================================================================================
CLASSIFICATION RESULTS
================================================================================

Logistic Regression:
------------------------------------------------------------
  Accuracy:  0.5754
  Precision: 0.5763
  Recall:    0.5970
  F1-Score:  0.5864
  CV Accuracy: 0.5783 (+/- 0.0065)

SVM (Linear):
------------------------------------------------------------
  Accuracy:  0.5831
  Precision: 0.5825
  Recall:    0.6117
  F1-Score:  0.5968
  CV Accuracy: 0.5860 (+/- 0.0068)

SVM (RBF):
------------------------------------------------------------
  Accuracy:  0.5926
  Precision: 0.5955
  Recall:    0.5992
  F1-Score:  0.5973
  CV Accuracy: 0.6071 (+/- 0.0091)

Random Forest:
------------------------------------------------------------
  Accuracy:  0.5958
  Precision: 0.6011
  Recall:    0.5898
  F1-Score:  0.5954
  CV Accuracy: 0.5997 (+/- 0.0076)

Neural Network:
------------------------------------------------------------
  Accuracy:  0.6009
  Precision: 0.5875
  Recall:    0.7009
  F1-Score:  0.6392
  CV Accuracy: 0.6036 (+/- 0.0087)

Gradient Boosting:
------------------------------------------------------------
  Accuracy:  0.6046
  Precision: 0.6043
  Recall:    0.6252
  F1-Score:  0.6146
  CV Accuracy: 0.6094 (+/- 0.0077)

Naive Bayes:
------------------------------------------------------------
  Accuracy:  0.5641
  Precision: 0.5919
  Recall:    0.4371
  F1-Score:  0.5028
  CV Accuracy: 0.5683 (+/- 0.0051)

K-Nearest Neighbors:
------------------------------------------------------------
  Accuracy:  0.5784
  Precision: 0.5815
  Recall:    0.5849
  F1-Score:  0.5832
  CV Accuracy: 0.5899 (+/- 0.0056)

================================================================================
SUMMARY TABLE
================================================================================
         Classifier  Accuracy  Precision   Recall       F1  CV_Mean   CV_Std
Logistic Regression  0.575429   0.576308 0.596955 0.586450 0.578350 0.006494
       SVM (Linear)  0.583107   0.582516 0.611733 0.596767 0.586029 0.006750
          SVM (RBF)  0.592593   0.595461 0.599194 0.597321 0.607092 0.009068
      Random Forest  0.595754   0.601095 0.589790 0.595389 0.599694 0.007645
     Neural Network  0.600949   0.587462 0.700851 0.639167 0.603647 0.008720
  Gradient Boosting  0.604562   0.604329 0.625168 0.614572 0.609407 0.007729
        Naive Bayes  0.564137   0.591874 0.437080 0.502834 0.568299 0.005058
K-Nearest Neighbors  0.578365   0.581478 0.584863 0.583166 0.589926 0.005623

================================================================================
PERMUTATION TEST (Statistical Validation)
================================================================================

Testing: Gradient Boosting
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

Real model accuracy: 0.6046
Mean permuted accuracy: 0.4991
Std permuted accuracy: 0.0165
p-value: 0.0000
✓ Model is significantly better than chance (p < 0.05)

✓ Visualization saved as 'classification_results.png'

================================================================================
FEATURE IMPORTANCE
================================================================================
  V: 0.2974
  S: 0.1940
  W: 0.1571
  F: 0.2534
  C: 0.0982
✓ Feature importance plot saved as 'feature_importance.png'

✓ Results saved to 'classification_results.csv'

================================================================================
CLASSIFICATION COMPLETE
================================================================================



