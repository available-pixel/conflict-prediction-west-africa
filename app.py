# app.py
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import plotly.express as px

# Custom CSS for background color/gradient
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #f0f4f8, #d9e2ec);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Load data
# -----------------------------
model = joblib.load("data/processed/rf_conflict_model.pkl")
predictions = pd.read_csv("data/processed/predicted_conflict_events.csv")
dataset = pd.read_csv("data/processed/conflict_dataset.csv")

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="AI Conflict Prediction", layout="wide")
st.title("🌍 AI-Powered Conflict Prediction in West Africa")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "📊 Dashboard",
    "🔮 Custom Prediction",
    "🗺️ Conflict Map",
    "📈 Trend Analysis"
])

# =====================================================
# 📊 DASHBOARD
# =====================================================
if page == "📊 Dashboard":
    st.header("Conflict Prediction Overview")

    country = st.selectbox("Select Country", sorted(predictions['Country'].unique()))
    year = st.selectbox("Select Year", sorted(predictions['Year'].unique()))

    value = int(predictions[
        (predictions['Country'] == country) &
        (predictions['Year'] == year)
    ]['Predicted_ConflictEvents'].values[0])

    st.metric("Predicted Conflict Events", value)

    # Bar chart
    pivot = predictions.pivot(index="Country", columns="Year", values="Predicted_ConflictEvents")
    pivot = pivot.sort_values(by=2027, ascending=False)

    fig = px.bar(pivot, barmode="group", title="2024 vs 2027 Predictions")
    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# 🔮 CUSTOM PREDICTION
# =====================================================
elif page == "🔮 Custom Prediction":
    st.header("Predict Conflict Events (Custom Input)")

    gdp = st.number_input("GDP", value=10000000000)
    population = st.number_input("Population", value=10000000)
    unemployment = st.slider("Unemployment (%)", 0.0, 50.0, 5.0)
    poverty = st.slider("Poverty Rate (%)", 0.0, 100.0, 40.0)
    temp = st.slider("Average Temperature (°C)", 20.0, 35.0, 27.0)
    rainfall = st.number_input("Rainfall (mm)", value=1200)

    if st.button("Predict"):
        input_data = pd.DataFrame([{
            "GDP": gdp,
            "Population": population,
            "Unemployment": unemployment,
            "PovertyRate": poverty,
            "AvgTemp": temp,
            "Rainfall": rainfall
        }])

        prediction = model.predict(input_data)[0]
        prediction = int(round(prediction))

        st.success(f"Predicted Conflict Events: {prediction}")

# =====================================================
# 🗺️ CONFLICT MAP
# =====================================================
elif page == "🗺️ Conflict Map":
    st.header("Conflict Intensity Map (2027)")

    map_data = predictions[predictions["Year"] == 2027]

    fig = px.choropleth(
        map_data,
        locations="Country",
        locationmode="country names",
        color="Predicted_ConflictEvents",
        color_continuous_scale="Reds",
        title="Predicted Conflict Events in 2027"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# 📈 TREND ANALYSIS
# =====================================================
elif page == "📈 Trend Analysis":
    st.header("Conflict Trend Over Time")

    country = st.selectbox("Select Country", sorted(dataset['Country'].unique()))

    country_data = dataset[dataset['Country'] == country]

    fig, ax = plt.subplots()
    ax.plot(country_data["Year"], country_data["ConflictEvents"], marker='o')
    ax.set_title(f"Conflict Trend - {country}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Conflict Events")

    st.pyplot(fig)

    st.write("Historical Data:")
    st.dataframe(country_data)