
---

# 📊 Credit Risk Modeling & Deployment (End-to-End ML Project)

## 🔍 Project Overview

This project builds a **production-ready Credit Risk Modeling system** using real-world financial data.
The system predicts the **probability of loan default** and makes **business-optimized approval/rejection decisions**, with full **explainability** and **API deployment**.

The project follows **industry-standard ML lifecycle practices**, including:

* Feature engineering
* Model evaluation using ROC-AUC
* Cost-sensitive threshold optimization
* ML pipelines
* FastAPI deployment
* Docker containerization

---

## 🧠 Business Problem

Financial institutions must decide whether to **approve or reject loans** while minimizing financial loss.

Challenges:

* Highly imbalanced data (~8% defaulters)
* Accuracy is misleading
* Wrong approvals (defaulters) are far more costly than rejections

### Objective:

Predict the **probability of default** and convert it into a **business decision** using a **cost-optimized threshold**.

---

## 📂 Dataset

**Home Credit Default Risk Dataset (Kaggle)**

* ~300,000 loan applications
* 120+ features
* Real banking data

Target variable:

* `TARGET = 1` → Loan defaulted
* `TARGET = 0` → Loan repaid

---

## 🛠️ Tech Stack

* **Python 3.11**
* **Pandas, NumPy**
* **Scikit-learn**
* **FastAPI**
* **Docker**
* **Uvicorn**
* **Joblib**

---

## 🧩 Project Architecture

```
credit-risk-project/
│
├── notebooks/
│   └── credit_risk_modeling.ipynb   # Phase 1–9 (EDA → Modeling → Pipeline)
│
├── api/
│   ├── main.py                      # FastAPI app (Phase 10)
│   ├── credit_risk_pipeline.pkl     # Saved ML pipeline
│   ├── requirements.txt
│   └── Dockerfile
│
├── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Cleaning & EDA

* Handled missing values using domain-driven logic
* Removed leakage-prone and high-missing columns
* Addressed real-world data quirks (employment placeholders)

### 2️⃣ Feature Engineering (Core Strength)

* Credit-to-income ratio
* Annuity-to-income ratio
* Employment stability metrics
* Log-transformed skewed financial features

### 3️⃣ Modeling

* Baseline: Logistic Regression
* Advanced: Random Forest, Gradient Boosting
* Evaluation metric: **ROC-AUC (industry standard)**

### 4️⃣ Business Threshold Optimization

* Converted probabilities into decisions
* Used cost-sensitive loss function
* Optimized rejection threshold (not fixed at 0.5)

### 5️⃣ ML Engineering

* Built `ColumnTransformer + Pipeline`
* Ensured training-inference consistency
* Saved full pipeline for deployment

---

## 🚀 FastAPI Deployment

### API Endpoints

| Method | Endpoint   | Description                     |
| ------ | ---------- | ------------------------------- |
| GET    | `/`        | Health check                    |
| POST   | `/predict` | Predict default risk & decision |

### Sample Request

```json
{
  "CODE_GENDER": "M",
  "AMT_INCOME_TOTAL": 180000,
  "AMT_CREDIT": 600000,
  "AMT_ANNUITY": 22000,
  "DAYS_BIRTH": -12000,
  "DAYS_EMPLOYED": -3000,
  "NAME_EDUCATION_TYPE": "Higher education",
  "NAME_FAMILY_STATUS": "Married",
  "NAME_INCOME_TYPE": "Working"
}
```

### Sample Response

```json
{
  "default_probability": 0.2874,
  "decision": "APPROVE",
  "threshold_used": 0.32
}
```

---

## 🐳 Dockerization (Production Ready)

### 🔹 Dockerfile (Copy-Paste)

Create `api/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY credit_risk_pipeline.pkl .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### 🔹 Build Docker Image

```bash
docker build -t credit-risk-api .
```

---

### 🔹 Run Docker Container

```bash
docker run -p 8000:8000 credit-risk-api
```

Open browser:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Key Results

* ROC-AUC: **~0.78**
* Accuracy: **~82–91%**
* Significant reduction in financial loss using cost-optimized threshold

---

## 🧪 Why This Project Is Job-Ready

✔ Real business problem
✔ Large-scale dataset
✔ Proper ML metrics
✔ Production pipeline
✔ REST API deployment
✔ Dockerized service

---

## 🧾 Resume-Ready Description

> Built an end-to-end Credit Risk Modeling system using large-scale financial data; performed domain-driven feature engineering, trained Gradient Boosting models optimized with ROC-AUC, implemented cost-sensitive decision thresholds and deployed the solution via FastAPI and Docker.

---

## 🚀 Future Improvements

* Model monitoring & data drift detection
* CI/CD pipeline
* Cloud deployment (AWS/GCP)
* Batch inference support

---

## 🤝 Author

**Jestu Ashok**
Aspiring Data Scientist | ML Engineer | AI Engineer

---


