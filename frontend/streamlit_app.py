import streamlit as st
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 100%
    );
}

/* Main Container */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Title */
.title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0.5rem;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.2rem;
    margin-bottom: 3rem;
}

/* Labels */
label {
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 14px !important;
    color: white !important;
}

/* Selectbox text */
div[data-baseweb="select"] span {
    color: white !important;
}

/* Number Input */
.stNumberInput input {
    background: #1e293b !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 14px !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 60px;
    background: linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    );
    color: white;
    border: none;
    border-radius: 14px;
    font-size: 20px;
    font-weight: 700;
}

.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #1d4ed8,
        #1e40af
    );
    color: white;
}

/* Result Card */
.result-card {
    margin-top: 25px;
    background: linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    );
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
}

.result-card h2 {
    margin-bottom: 10px;
}

.result-price {
    font-size: 2.5rem;
    font-weight: 800;
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    """
    <h1 class="title">🚗 Car Price Predictor</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="subtitle">
    Predict the resale value of your car using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- FORM ---------------- #

col1, col2 = st.columns(2)

with col1:

    brand = st.selectbox(
        "Brand",
        [
            "Maruti",
            "Hyundai",
            "Honda",
            "Toyota",
            "Ford",
            "Mahindra",
            "Tata"
        ]
    )

    year = st.selectbox(
        "Manufacturing Year",
        list(range(2025, 1990, -1))
    )

    fuel = st.selectbox(
        "Fuel Type",
        [
            "Petrol",
            "Diesel",
            "CNG",
            "LPG"
        ]
    )

with col2:

    seller_type = st.selectbox(
        "Seller Type",
        [
            "Individual",
            "Dealer",
            "Trustmark Dealer"
        ]
    )

    transmission = st.selectbox(
        "Transmission",
        [
            "Manual",
            "Automatic"
        ]
    )

    owner = st.selectbox(
        "Owner",
        [
            "First Owner",
            "Second Owner",
            "Third Owner",
            "Fourth & Above Owner"
        ]
    )

km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=50000,
    step=1000
)

st.write("")

predict = st.button("🚀 Predict Price")

# ---------------- PREDICTION ---------------- #

if predict:

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
            "https://car-price-predictor-n8wh.onrender.com/predict",
            json=payload,
            timeout=30
        )

        if response.status_code == 200:

            prediction = response.json()["predicted_price"]

            st.markdown(
                f"""
                <div class="result-card">
                    <h2>Estimated Resale Price</h2>
                    <div class="result-price">
                        ₹ {prediction:,.0f}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.error(f"API Error: {response.text}")

    except Exception as e:
        st.error(f"Connection Error: {e}")