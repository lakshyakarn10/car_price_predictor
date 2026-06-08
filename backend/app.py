from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("../models/model.pkl")
encoders = joblib.load("../models/encoders.pkl")


class CarInput(BaseModel):
    brand: str
    year: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str


@app.get("/")
def home():
    return {
        "message": "Car Price Prediction API running"
    }


@app.post("/predict")
def predict(car: CarInput):

    data = {
        "year": car.year,
        "km_driven": car.km_driven,
        "fuel": car.fuel,
        "seller_type": car.seller_type,
        "transmission": car.transmission,
        "owner": car.owner,
        "brand": car.brand
    }

    df = pd.DataFrame([data])

    categorical_cols = [
        "brand",
        "fuel",
        "seller_type",
        "transmission",
        "owner"
    ]

    for col in categorical_cols:
        df[col] = encoders[col].transform(df[col])

    # Force exact training column order
    df = df[
        [
            "year",
            "km_driven",
            "fuel",
            "seller_type",
            "transmission",
            "owner",
            "brand"
        ]
    ]

    print("Columns:", df.columns.tolist())

    prediction = model.predict(df)

    return {
        "predicted_price": round(float(prediction[0]), 2)
    }