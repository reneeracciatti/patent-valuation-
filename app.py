import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model/patent_model.pkl")

# App title
st.title("📊 Patent Valuation AI")

# Input form
with st.form("patent_input"):
    st.header("Enter Patent Details")
    citations = st.number_input("Citation Count", min_value=0, value=20)
    lawsuits = st.number_input("Active Lawsuits", min_value=0, value=1)
    inv_rate = st.slider("Invalidation Rate", 0.0, 1.0, 0.5)
    industry_growth = st.slider("Industry Growth (%)", 0.0, 10.0, 5.0)
    submitted = st.form_submit_button("Calculate Value")

# When user submits
if submitted:
    # Predict value
    input_data = pd.DataFrame([[citations, lawsuits, inv_rate, industry_growth]],
                             columns=["citations", "lawsuits", "invalidation_rate", "industry_growth"])
    predicted_value = model.predict(input_data)[0]

    # Display results
    st.subheader("📈 Valuation Results")
    st.success(f"Estimated Patent Value: **${predicted_value:,.2f}**")

    # Calculate risk score (simplified)
    risk_score = min(100, (lawsuits * 20) + (inv_rate * 50))
    st.warning(f"⚠️ Risk Score: **{risk_score}/100**")

if jurisdiction == "Texas":
    risk_score += 30  # Texas courts are higher risk
    st.write("⚠️ Warning: Texas courts have higher invalidation rates")
