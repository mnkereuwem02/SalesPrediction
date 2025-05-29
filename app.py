import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and preprocessing tools
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("encoders.pkl")  # dictionary of LabelEncoders

shipping_location_cost = {
    'Austin': [0], 'Cardiff': [40], 'Cleveland': [0], 'Detroit': [0], 'Dublin': [40],
    'Glasgow': [40], 'Las Vegas': [0], 'Liverpool': [40], 'London': [40], 'Manchester': [40],
    'Memphis': [0], 'Miami': [0], 'Montreal': [25], 'Mumbai': [70], 'New Delhi': [70],
    'New Jersey': [0], 'New York': [0], 'Paris': [50], 'Pittsburgh': [0], 'Portland': [0],
    'Sacramento': [0], 'San Antonio': [0], 'San Francisco': [0], 'Sydney': [100], 'Toronto': [25]
}

st.title("Sales Prediction Application")

# Input widgets
Gender = st.selectbox('Gender', ['Female', 'Male'])
Age = st.number_input('Age', min_value=18)
Location = st.selectbox('Order Location', list(shipping_location_cost.keys()))
Category = st.selectbox('Product Category', ['Clothing', 'Other', 'Ornaments'])
Price = st.number_input('Sales Price', min_value=0.0, max_value=5000.0, value=5.0, step=0.01)
Quantity = st.number_input('Quantity', min_value=0)
Sales_per_unit = Price / Quantity if Quantity != 0 else 0
st.write(f"Sales Per Unit: {Sales_per_unit}")
International_shipping = st.radio('International_shipping', ["Yes", "No"])

# Fix: assign Shipping_Charges for both cases
if International_shipping == 'Yes':
    Shipping_Charges = st.selectbox('Shipping_Charges', shipping_location_cost[Location])
else:
    Shipping_Charges = 0  # default if not international

Rating = st.number_input('Rating', min_value=0, max_value=5)
Order_year = st.selectbox('Order Year', [i for i in range(2020, 2051)])

# Predict button
if st.button("Predict Sales"):
    input_data = pd.DataFrame({
        'Gender': [Gender],
        'Age': [Age],
        'Order Location': [Location],
        'Product Category': [Category],
        'Sales Price': [Price],
        'Quantity': [Quantity],
        'Sales_per_unit': [Sales_per_unit],
        'International_shipping': [International_shipping],
        'Shipping_Charges': [Shipping_Charges],
        'Rating': [Rating],
        'Order Year': [Order_year]
    })

    # List of categorical columns
    categorical_cols = ['Gender', 'Order Location', 'Product Category', 'International_shipping']

    # Encode each categorical column using its LabelEncoder
    for col in categorical_cols:
        if col in input_data.columns:
            input_data[col] = label_encoders[col].transform(input_data[col])

    # Scale features
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Sales: {prediction[0]}")
