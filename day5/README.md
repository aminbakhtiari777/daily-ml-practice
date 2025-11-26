ex_day5_week5

## Wine Classification using SVM (Support Vector Machine)

In this exercise, we built and evaluated a Support Vector Machine (SVM) model to classify different types of wine.

### What was done in this project:

- Loaded and explored the **Wine dataset** from a CSV file.
- Separated the dataset into:
  - Features (`X`)
  - Target labels (`y`)
- Split the data into **training (80%)** and **testing (20%)** sets with stratification.
- Built a machine learning pipeline including:
  - `StandardScaler` for feature normalization
  - `SVC` with **RBF kernel** for classification
- Trained the model on the training data.
- Evaluated model performance using:
  - Accuracy score
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-score)
- Applied **GridSearchCV** to tune hyperparameters:
  - Optimized `C` and `gamma` values for better performance
  - Used 5-fold cross-validation
- Selected the best model and evaluated it on the test set.

This exercise demonstrates the complete workflow of:
Data preprocessing → Model training → Hyperparameter tuning → Final evaluation.
