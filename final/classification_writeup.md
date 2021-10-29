# Loan Default Classification

Manveer Sadhal

## Abstract
The goal of this project was to create a classification model to identify loans in Interested Lending, Inc.'s portfolio of issued loans which are likely to default. This model would have several use cases for a lender - prompting outreach to the borrower, identifying loans which could be sold to another institution, and predicting the rate of loan defaults as part of the lender's operating plan. Insights from the model could also be used to improve the loan approval process.

[A data set with approximately 887,000 loans](https://www.kaggle.com/ranadeep/credit-risk-dataset) was obtained from Kaggle.com.

## Design
Accurate assessment of credit default risk is a vital component in lender operations. Borrowers are screened prior to being granted a loan, but following loan issuance a risk remains of the borrower's circumstances changing and the loan not being repaid. Evaluating approved loans which terminated without being fully repaid also has utility in improving the loan approval process as screening parameters may need to be adjusted over time.

## Data
A data set containing a snapshot of approximately 887,000 loans was used to develop the classification model. Only loans which had closed (whether by repayment or default) were considered. After cleaning, approximately 250,000 loans remained for model development.

The original data set contained 73 columns. A smaller data set with 19 columns was created after removing features which were irrelevant, would introduce leakage from the target, or contained a high proportion of null values.

## Algorithms
### Feature Engineering
1. One-hot encoding the loan term and loan grade categorical features.
2. Evaluating correlation coefficients between numeric features and the target.

### Model Selection
Logistic regression was used as a baseline model. K-nearest neighbors, random forest, and XGBoost models were also evaluated. KNN was the least performant model and was removed from consideration. Random forest and XGBoost models had extremely similar performance to the logistic regression model. Since logistic regression offers better interpretability, it was chosen over the more complex models.

### Model Tuning and Evaluation
20% of the data set was split off as the test (holdout) set and not evaluated until all model development was completed.

The remaining data set was split into training and validation sets so that precision, recall, and could be evaluated on the validation set with models trained on the training set.

SciKit-Learn's RandomizedSearchCV was used to evaluate a wide range of parameters (regularization strength, max iterations, penalty). With the best parameters from the randomized search, the model was tuned further in a narrow range with GridSearchCV using five-fold cross-validation. The final model was created using the best parameters from the grid search, trained on the training + validation data splits, and scored on the test split.

### Interactive App
A Streamlit app was created using a pickled version of the final model. Users can enter information for a given loan and get an instant classification result from the model.

## Tools
- Data Cleaning
    - Pandas
    - NumPy
- Model Development and Testing
    - SciKit-Learn
- Visualization
    - Matplotlib
    - Seaborn
- Production
    - Streamlit interactive app

## Communication
A summary of the modeling process and results will be communicated during a 5-minute slide presentation.