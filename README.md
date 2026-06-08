# 🚗 Car Price Predictor

A Machine Learning web application that predicts the resale price of a used car based on various features such as brand, year, fuel type, transmission, ownership history, and kilometers driven.

Built using **XGBoost**, **FastAPI**, and **Streamlit**.

---

## 📌 Features

* Predict used car prices instantly
* User-friendly Streamlit interface
* FastAPI backend for model serving
* XGBoost Regression model
* Real-time predictions
* Responsive and modern UI
* Dropdown-based input selection

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Model Persistence

* Joblib

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
car-price-predictor/

├── backend/
│   ├── app.py
│   ├── render.yaml
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── .streamlit/
│       └── config.toml
│
├── models/
│   ├── model.pkl
│   └── encoders.pkl
│
├── notebooks/
│   └── training.ipynb
│
├── data/
│   └── cars.csv
│
├── .gitignore
└── README.md
```

---

## 📊 Dataset

The model was trained on Car Dekho dataset containing:

* Brand
* Manufacturing Year
* Kilometers Driven
* Fuel Type
* Seller Type
* Transmission Type
* Ownership History

### Target Variable

* Selling Price

---

## 🤖 Machine Learning Pipeline

### Data Preprocessing

* Handling missing values
* Label Encoding for categorical features
* Feature selection
* Train-Test Split

### Model Training

* XGBoost Regressor
* Model evaluation using R² Score

### Performance

```text
R² Score: 0.74
```

---

## 🚀 Running Locally

### Clone Repository

```bash
git clone https://github.com/lakshyakarn10/car_price_predictor.git
cd car_price_predictor
```

### Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Run FastAPI Server

```bash
uvicorn app:app --reload
```

### Install Frontend Dependencies

```bash
cd frontend
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Data preprocessing and feature engineering
* Regression modeling using XGBoost
* Building REST APIs with FastAPI
* Frontend development using Streamlit
* Model serialization with Joblib
* Git and GitHub workflow
* End-to-end ML project development

---

## 🔮 Future Improvements

* Advanced feature engineering
* Hyperparameter tuning
* Docker containerization
* Cloud deployment
* Analytics dashboard
* Price trend visualization
* Model explainability using SHAP

---

## 👨‍💻 Author

**Lakshya Karn**

B.Tech, NIT Rourkela

### Interests

* Machine Learning
* Data Science
* Deep Learning
* Full Stack AI Development

---
