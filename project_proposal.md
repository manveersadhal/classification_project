# Loan Default Classification

#### Manveer Sadhal
#### Oct 20, 2021

## Need
Interested Lending, Inc. is a small credit union. In order to help quantify the risk of current loans going into default, Interested Lending has hired an outside firm to develop a classification model.

The question this classification project intends to answer is whether a given borrower will default based on the information they submitted with their loan application as well as information about the loan to date.

## Data Description
### Data
The primary source of data will be the Kaggle.com ["Credit Risk Analysis" data set](https://www.kaggle.com/ranadeep/credit-risk-dataset). The data will be downloaded as a CSV file. The dataset contains approximately 887,000 records.

An individual sample will be a record of a single loan.

Possible features:
- FICO score
- Total debt
- Total income
- Interest rate of loan
- Total current balance
- Number of derogatory public records
- Late fees received to date
- Ratio of credit used to total credit
- Employment length
- Home ownership status
- Number of accounts borrower is delinquent on
- Number of times borrower has been delinquent over 30 days in the last two years

The target of the model will be whether or not the borrower will default on the loan.

### Algorithm
Multiple model types will be considered and rigorously evaluated to determine which is the most appropriate.

## Tools
- Data Cleaning
    - Pandas
    - NumPy
- Model Development and Testing
    - SciKit-Learn
- Visualization
    - Matplotlib
    - Seaborn
    - Plotly
- Production
    - Streamlit
    
## MVP Goal
Create a baseline model. Show that there is a relationship between at least some of the features and the target.

Brief text describing the model used, features considered, and initial metrics will be provided.