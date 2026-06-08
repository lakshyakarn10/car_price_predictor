import streamlit as st
import requests
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* App Background */
.stApp {
    background-color: #eef2f7;
}

/* Main White Card */
.main .block-container {
    background: white;
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    max-width: 900px;
}

/* Title */
h1 {
    text-align: center;
    color: #0f172a;
    font-size: 3rem;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Selectboxes */
div[data-baseweb="select"] > div {
    background-color: #f8fafc !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

/* Number Input */
.stNumberInput input {
    background-color: #f8fafc !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

/* Predict Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    background: #2563eb;
    color: white;
    border: none;
    font-size: 20px;
    font-weight: 600;
}

.stButton > button:hover {
    background: #1d4ed8;
    color: white;
}

/* Labels */
label {
    font-weight: 600 !important;
}

/* Result Card */
.result-card {
    background: #dcfce7;
    color: #166534;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD ENCODERS ---------------- #

encoders = joblib.load("../models/encoders.pkl")

brands = list(encoders["brand"].classes_)
fuels = list(encoders["fuel"].classes_)
seller_types = list(encoders["seller_type"].classes_)
transmissions = list(encoders["transmission"].classes_)
owners = list(encoders["owner"].classes_)

# ---------------- HEADER ---------------- #

st.title("🚗 Car Price Predictor")

st.markdown(
    """
    <p class="subtitle">
    Predict the resale value of your car using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- FORM ---------------- #

brand = st.selectbox(
    "Brand",
    brands
)

year = st.selectbox(
    "Year",
    list(range(2025, 1990, -1))
)

km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=50000,
    step=1000
)

fuel = st.selectbox(
    "Fuel Type",
    fuels
)

seller_type = st.selectbox(
    "Seller Type",
    seller_types
)

transmission = st.selectbox(
    "Transmission",
    transmissions
)

owner = st.selectbox(
    "Owner",
    owners
)

# ---------------- PREDICT ---------------- #

if st.button("📈 Predict Price"):

    payload = {
        "brand": brand,
        "year": int(year),
        "km_driven": int(km_driven),
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            st.markdown(
                f"""
                <div class="result-card">
                Predicted Price: ₹{result['predicted_price']:,.0f}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.error(f"API Error: {response.text}")

    except Exception as e:
        st.error(f"Connection Error: {e}")