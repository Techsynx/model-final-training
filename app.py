import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('water_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('💧 Water Potability Predictor')

st.markdown("Enter the water test results below to check if it's safe to drink.")

# User inputs
ph = st.number_input('pH', min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input('Hardness', min_value=0.0)
solids = st.number_input('Solids', min_value=0.0)
chloramines = st.number_input('Chloramines', min_value=0.0)
sulfate = st.number_input('Sulfate', min_value=0.0)
conductivity = st.number_input('Conductivity', min_value=0.0)
organic_carbon = st.number_input('Organic Carbon', min_value=0.0)
trihalomethanes = st.number_input('Trihalomethanes', min_value=0.0)
turbidity = st.number_input('Turbidity', min_value=0.0)

# Predict button
if st.button('Predict'):
    features = np.array([[ph, hardness, solids, chloramines, sulfate,
                          conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ This water is **potable** (safe to drink).")
    else:
        st.error("❌ This water is **not potable** (unsafe to drink).")
