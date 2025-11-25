import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("model.pkl")

st.title("💼 AI Salary Prediction System")
st.write("Enter the details below and get an AI-generated salary prediction.")

# Inputs
experience = st.number_input("Years of Experience", 0, 40, 3)
age = st.number_input("Age", 18, 60, 25)
education = st.selectbox("Education Level", ["Diploma", "Bachelor", "Master", "PhD"])
role = st.selectbox("Job Role", ["Developer", "Analyst", "Manager", "Tester", "Data Scientist"])
location_tier = st.selectbox("Location Tier", ["Tier-1", "Tier-2", "Tier-3"])
prev_company_rating = st.slider("Previous Company Rating", 2.5, 5.0, 4.0, 0.1)

skills = st.multiselect("Skills", ["Python","Java","SQL","Excel","ML","Cloud","C++","Communication"])

if st.button("Predict Salary"):
    skill_str = "|".join(skills)

    sample = {
        "experience": experience,
        "age": age,
        "education": education,
        "role": role,
        "location_tier": location_tier,
        "prev_company_rating": prev_company_rating,
        "skills": skill_str
    }

    # --- feature engineering (must match training code) ---
    sample_df = pd.DataFrame([sample])
    sample_df["skill_count"] = sample_df["skills"].apply(lambda x: len(x.split("|")) if x != "" else 0)

    for sk in ["Python","ML","Cloud","SQL"]:
        sample_df[f"skill_{sk.lower()}"] = sample_df["skills"].apply(lambda s: int(sk in s.split("|")))

    sample_df = sample_df.drop(columns=["skills"])

    predicted_salary = model.predict(sample_df)[0]

    st.success(f"Predicted Salary: ₹ {int(predicted_salary):,}")
