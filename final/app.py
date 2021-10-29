import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

#load pickled model

with open("lm.pkl", "rb") as f:
    lm = pkl.load(f)

st.title("Loan Default Classification")
st.write("Enter information below. Default prediction will be displayed at the bottom of the screen.")

#receive user input

annual_inc = st.number_input(label='Annual income (USD)', min_value=0, max_value=8700000, step=10000)
collections_12_mths_ex_med = st.number_input(label='Number of accounts in collections within past 12 months (excluding medical)', min_value=0, max_value=6, step=1)
delinq_2yrs = st.number_input(label='Number of delinquencies over 30 days in the last two years', min_value=0, max_value=29, step=1)
dti = st.number_input(label='Debt to income ratio', min_value=0, max_value=57)
inq_last_6mths = st.number_input(label='Credit inquiries in the last 6 months', min_value=0, max_value=33, step=1)
int_rate = st.number_input(label='Interest rate (%)', min_value=0.0, max_value=29.0, step=.5)
open_acc = st.number_input(label="Number of open credit lines in borrower's file", min_value=1, max_value=76, step=1)
pub_rec = st.number_input(label='Number of derogatory public records', min_value=0, max_value=15, step=1)
revol_util = st.number_input(label='Revolving debt utilization (%)', min_value=0, max_value=892, step=1)
total_acc = st.number_input(label="Total number of credit lines in borrower's file (open or closed)", min_value=1, max_value=150, step=1)
acc_now_delinq = st.number_input(label='Total number of accounts currently delinquent', min_value=0, max_value=5, step=1)
term = int(st.selectbox(label='Loan Term (months)', options=[36, 60]))
if term==36:
    term_60_months=1
else:
    term_60_months=0
grade = st.selectbox(label='Loan Grade', options=['A', 'B', 'C', 'D', 'E', 'F', 'G'])

grade_B = grade_C = grade_D = grade_E = grade_F = grade_G = 0
if grade == 'B':
    grade_B = 1
elif grade == 'C':
    grade_C = 1
elif grade == 'D':
    grade_D = 1
elif grade =='E':
    grade_E = 1
elif grade == 'F':
    grade_F = 1
elif grade == 'G':
    grade_G = 1

installment = st.number_input(label='Installment (USD)', min_value=15, max_value=1424, step=100)

model_inputs = np.array([
                annual_inc,
                collections_12_mths_ex_med,
                delinq_2yrs,
                dti,
                inq_last_6mths,
                int_rate,
                open_acc,
                pub_rec,
                revol_util,
                total_acc,
                acc_now_delinq,
                term_60_months,
                grade_B,
                grade_C,
                grade_D,
                grade_E,
                grade_F,
                grade_G,
                installment
                ])


#display model prediction
if lm.predict(model_inputs.reshape(1,-1))[0] == 0:
    st.write("""
    # Loan is not expected to default!
    """)
else:
    st.write("""
    # Loan is expected to default!
    """)
