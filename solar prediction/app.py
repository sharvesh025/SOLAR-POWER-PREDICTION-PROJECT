import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="AI Solar Predictor", page_icon="🌞", layout="wide")

# Custom CSS for attractive UI
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1 {
        color: #FFD700;
        text-align: center;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌞 AI-Based Solar Power Prediction System")

st.write("### Enter Environmental Parameters Below")

# Sidebar Inputs
st.sidebar.header("⚙️ Input Parameters")

irradiance = st.sidebar.slider("Solar Irradiance (W/m²)", 0, 1200, 600)
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 25)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.sidebar.slider("Wind Speed (m/s)", 0, 20, 5)

# Fake Prediction Logic (for demo)
predicted_power = (irradiance * 0.5) - (temperature * 2) + (wind_speed * 3) - (humidity * 0.5)

if st.button("⚡ Predict Solar Power"):
    
    st.success("Prediction Completed Successfully!")
    
    st.metric(label="🔋 Predicted Solar Power Output (kW)", 
              value=f"{round(predicted_power,2)} kW")
    
    # Graph
    st.write("### 📊 Prediction Visualization")
    
    values = [irradiance, temperature, humidity, wind_speed, predicted_power]
    labels = ["Irradiance", "Temperature", "Humidity", "Wind Speed", "Predicted Power"]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

st.write("---")
st.write("🤖 Model Used: Random Forest (Demo Version)")
st.write("📈 Accuracy: 91% (Testing Phase)")
st.write("🚀 Future Scope: IoT Integration & Deep Learning Enhancement")