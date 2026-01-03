from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained ML pipeline
credit_risk_pipeline = joblib.load("credit_risk_pipeline.pkl")

BUSINESS_THRESHOLD = 0.32

# FastAPI app
app = FastAPI(
    title="Credit Risk Prediction API",
    description="Predict probability of loan default and decision",
    version="1.0"
)

class CreditApplication(BaseModel):
    CODE_GENDER: str
    NAME_EDUCATION_TYPE: str
    NAME_FAMILY_STATUS: str
    NAME_INCOME_TYPE: str

    AGE_YEARS: float
    EMPLOYED_YEARS: float
    EMPLOYMENT_AGE_RATIO: float

    TOTAL_INCOME: float
    CREDIT_INCOME_RATIO: float
    ANNUITY_INCOME_RATIO: float
    CREDIT_TERM_YEARS: float



@app.get("/")
def home():
    return {"status": "Credit Risk API is running"}

@app.post("/predict")
def predict_risk(data: CreditApplication):

    input_df = pd.DataFrame([data.dict()])

    default_probability = credit_risk_pipeline.predict_proba(input_df)[0][1]

    decision = "REJECT" if default_probability >= BUSINESS_THRESHOLD else "APPROVE"

    return {
        "default_probability": round(float(default_probability), 4),
        "decision": decision,
        "threshold_used": BUSINESS_THRESHOLD
    }

