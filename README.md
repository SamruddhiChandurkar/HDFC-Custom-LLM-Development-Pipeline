# HDFC Custom LLM Development Pipeline
## Academic Prototype

### Overview

This project demonstrates a governed AI workflow
for a synthetic banking use case.

### Features

- Dataset validation and intake
- Persistent dataset registry
- Dataset approval workflow
- Audit logging
- Synthetic banking knowledge base
- Retrieval-based loan assistant
- Safety fallback
- FastAPI backend
- Streamlit interface
- Automated tests

### Architecture

User
  |
Streamlit Dashboard
  |
FastAPI Backend
  |
Loan Assistant
  |
Knowledge Retrieval
  |
Synthetic FAQ Knowledge Base

Dataset Intake
  |
Validation
  |
Registry
  |
Approval
  |
Audit Log

### Run Project

Install dependencies:

pip install -r requirements.txt

Start API:

python -m uvicorn src.api:app --reload

Start dashboard:

streamlit run app.py

### API Documentation

http://127.0.0.1:8000/docs

### Testing

pytest -v

### Limitations

This is a local academic prototype.
It does not use real customer information,
perform actual loan underwriting, or represent
an official bank deployment.