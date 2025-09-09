# Create an interactive loan calculator application using Streamlit and Python,
# where users can input multiple details such as name, age, deposit, interest, 
# duration, and more. Use different input types such as text, numbers, toggles, 
# sliders, and checkboxes, and return the results with multiple graphs and 
# dataframes. Finally, deploy the web app on Streamlit Cloud. and submit both 
# github repo and live website URL


import streamlit as st
import pandas as pd

st.title("Loan Calculator Application")
st.write("An interactive loan calculator built with Streamlit.")

name = st.text_input("Enter your Name")
if st.button("Submit"):
    result = name.title()  
    st.success(result)

age = st.number_input("Enter your Age", min_value=18, max_value=100, step=1)

deposit = st.number_input("Deposit Amount (₹)", min_value=0, step=1000)

loan_amount = st.number_input("Loan Amount (₹)", min_value=1000, step=1000)

interest_rate = st.slider("Interest Rate (%)", min_value=1.0, max_value=20.0, value=8.0)

duration_years = st.slider("Loan Duration (Years)", min_value=1, max_value=30, value=5)


# Loan Calculation 
monthly_rate = interest_rate / 100 / 12
months = duration_years * 12

# EMI Formula
if loan_amount > 0 and monthly_rate > 0:
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
else:
    emi = 0

total_payment = emi * months
total_interest = total_payment - loan_amount

# Results 
st.subheader("Loan Summary")
st.write(f"Hello **{name}**, here are your loan details:")

summary = {
    "Loan Amount (₹)": loan_amount,
    "Deposit (₹)": deposit,
    "Interest Rate (%)": interest_rate,
    "Duration (Years)": duration_years,
    "Monthly EMI (₹)": round(emi, 2),
    "Total Payment (₹)": round(total_payment, 2),
    "Total Interest (₹)": round(total_interest, 2)
}

if st.button("Show Loan Summary"):
    st.dataframe(pd.DataFrame([summary]))

# Amortization Schedule 
st.subheader(" Amortization Schedule")
schedule = []
balance = loan_amount
for m in range(1, months + 1):
    interest = balance * monthly_rate
    principal = emi - interest 
    balance = max(balance - principal, 0)
    schedule.append([m, round(principal, 2), round(interest, 2), round(balance, 2)])
    if balance <= 0:
        break

df_schedule = pd.DataFrame(schedule, columns=["Month", "Principal Paid", "Interest Paid", "Remaining Balance"])
if st.button("Show Amortization Schedule"):
    st.dataframe(df_schedule.head(12))

st.success(" Loan calculation complete!")

# url -- http://localhost:8501/
