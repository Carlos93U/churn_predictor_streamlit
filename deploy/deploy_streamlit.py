import pickle

import pandas as pd
import streamlit as st

with open("models/churn_model.pkl", "rb") as f:
    trained_model = pickle.load(f)

st.set_page_config(page_title="Churn Predictor")

st.title("Churn Predictor Model")

st.write(
    "Enter values about features to get a prediction."
)

# Get input data from user
SeniorCitizen = st.number_input("Senior Citizen:", value=0, min_value=0, max_value=1)
tenure = st.number_input("Tenure:", value=0, min_value=0, max_value=100)
MonthlyCharges = st.number_input("Monthly Charges:", value=0.0, min_value=0.0, max_value=9999.99)
TotalCharges = st.number_input("Total Charges:", value=0.0, min_value=0.0, max_value=99999.99)
Partner_No = st.number_input("Partner (No):", value=0, min_value=0, max_value=1)
Partner_Yes = st.number_input("Partner (Yes):", value=0, min_value=0, max_value=1)
Dependents_No = st.number_input("Dependents (No):", value=0, min_value=0, max_value=1)
Dependents_Yes = st.number_input("Dependents (Yes):", value=0, min_value=0, max_value=1)
MultipleLines_No = st.number_input("Multiple Lines (No):", value=0, min_value=0, max_value=1)
MultipleLines_No_phone_service = st.number_input("Multiple Lines (No phone service):", value=0, min_value=0, max_value=1)
MultipleLines_Yes = st.number_input("Multiple Lines (Yes):", value=0, min_value=0, max_value=1)
InternetService_DSL = st.number_input("Internet Service (DSL):", value=0, min_value=0, max_value=1)
InternetService_Fiber_optic = st.number_input("Internet Service (Fiber optic):", value=0, min_value=0, max_value=1)
InternetService_No = st.number_input("Internet Service (No):", value=0, min_value=0, max_value=1)
OnlineSecurity_No = st.number_input("Online Security (No):", value=0, min_value=0, max_value=1)
OnlineSecurity_No_internet_service = st.number_input("Online Security (No internet service):", value=0, min_value=0, max_value=1)
OnlineSecurity_Yes = st.number_input("Online Security (Yes):", value=0, min_value=0, max_value=1)
OnlineBackup_No = st.number_input("Online Backup (No):", value=0, min_value=0, max_value=1)
OnlineBackup_No_internet_service = st.number_input("Online Backup (No internet service):", value=0, min_value=0, max_value=1)
OnlineBackup_Yes = st.number_input("Online Backup (Yes):", value=0, min_value=0, max_value=1)
DeviceProtection_No = st.number_input("Device Protection (No):", value=0, min_value=0, max_value=1)
DeviceProtection_No_internet_service = st.number_input("Device Protection (No internet service):", value=0, min_value=0, max_value=1)
DeviceProtection_Yes = st.number_input("Device Protection (Yes):", value=0, min_value=0, max_value=1)
TechSupport_No = st.number_input("Tech Support (No):", value=0, min_value=0, max_value=1)
TechSupport_No_internet_service = st.number_input("Tech Support (No internet service):", value=0, min_value=0, max_value=1)
TechSupport_Yes = st.number_input("Tech Support (Yes):", value=0, min_value=0, max_value=1)
StreamingTV_No = st.number_input("Streaming TV (No):", value=0, min_value=0, max_value=1)
StreamingTV_No_internet_service = st.number_input("Streaming TV (No internet service):", value=0, min_value=0, max_value=1)
StreamingTV_Yes = st.number_input("Streaming TV (Yes):", value=0, min_value=0, max_value=1)
StreamingMovies_No = st.number_input("Streaming Movies (No):", value=0, min_value=0, max_value=1)
StreamingMovies_No_internet_service = st.number_input("Streaming Movies (No internet service):", value=0, min_value=0, max_value=1)
StreamingMovies_Yes = st.number_input("Streaming Movies (Yes):", value=0, min_value=0, max_value=1)
Contract_Month_to_month = st.number_input("Contract (Month-to-month):", value=0, min_value=0, max_value=1)
Contract_One_year = st.number_input("Contract (One year):", value=0, min_value=0, max_value=1)
Contract_Two_year = st.number_input("Contract (Two year):", value=0, min_value=0, max_value=1)
PaperlessBilling_No = st.number_input("Paperless Billing (No):", value=0, min_value=0, max_value=1)
PaperlessBilling_Yes = st.number_input("Paperless Billing (Yes):", value=0, min_value=0, max_value=1)
PaymentMethod_Bank_transfer_automatic = st.number_input("Payment Method (Bank transfer automatic):", value=0, min_value=0, max_value=1)
PaymentMethod_Credit_card_automatic = st.number_input("Payment Method (Credit card automatic):", value=0, min_value=0, max_value=1)
PaymentMethod_Electronic_check = st.number_input("Payment Method (Electronic check):", value=0, min_value=0, max_value=1)
PaymentMethod_Mailed_check = st.number_input("Payment Method (Mailed check):", value=0, min_value=0, max_value=1)


input_data = pd.DataFrame(
    [
        {
            "SeniorCitizen": SeniorCitizen,
            "tenure": tenure,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges,
            "Partner_No": Partner_No,
            "Partner_Yes": Partner_Yes,
            "Dependents_No": Dependents_No,
            "Dependents_Yes": Dependents_Yes,
            "MultipleLines_No": MultipleLines_No,
            "MultipleLines_No phone service": MultipleLines_No_phone_service,
            "MultipleLines_Yes": MultipleLines_Yes,
            "InternetService_DSL": InternetService_DSL,
            "InternetService_Fiber optic": InternetService_Fiber_optic,
            "InternetService_No": InternetService_No,
            "OnlineSecurity_No": OnlineSecurity_No,
            "OnlineSecurity_No internet service": OnlineSecurity_No_internet_service,
            "OnlineSecurity_Yes": OnlineSecurity_Yes,
            "OnlineBackup_No": OnlineBackup_No,
            "OnlineBackup_No internet service": OnlineBackup_No_internet_service,
            "OnlineBackup_Yes": OnlineBackup_Yes,
            "DeviceProtection_No": DeviceProtection_No,
            "DeviceProtection_No internet service": DeviceProtection_No_internet_service,
            "DeviceProtection_Yes": DeviceProtection_Yes,
            "TechSupport_No": TechSupport_No,
            "TechSupport_No internet service": TechSupport_No_internet_service,
            "TechSupport_Yes": TechSupport_Yes,
            "StreamingTV_No": StreamingTV_No,
            "StreamingTV_No internet service": StreamingTV_No_internet_service,
            "StreamingTV_Yes": StreamingTV_Yes,
            "StreamingMovies_No": StreamingMovies_No,
            "StreamingMovies_No internet service": StreamingMovies_No_internet_service,
            "StreamingMovies_Yes": StreamingMovies_Yes,
            "Contract_Month-to-month": Contract_Month_to_month,
            "Contract_One year": Contract_One_year,
            "Contract_Two year": Contract_Two_year,
            "PaperlessBilling_No": PaperlessBilling_No,
            "PaperlessBilling_Yes": PaperlessBilling_Yes,
            "PaymentMethod_Bank transfer (automatic)": PaymentMethod_Bank_transfer_automatic,
            "PaymentMethod_Credit card (automatic)": PaymentMethod_Credit_card_automatic,
            "PaymentMethod_Electronic check": PaymentMethod_Electronic_check,
            "PaymentMethod_Mailed check": PaymentMethod_Mailed_check
        }
    ]
)


# Make prediction
prediction = trained_model.predict(input_data)

# Display prediction
st.write("Prediction:", prediction[0])
