
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.data_validator import validate_dataset


# Create FastAPI application
app = FastAPI(
    title="HDFC Custom LLM Pipeline API",
    description="Demo API for banking dataset governance",
    version="1.0.0"
)


# Find project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Demo dataset location
DATASET_PATH = PROJECT_ROOT / "data" / "banking_records.json"

REGISTRY_PATH = PROJECT_ROOT / "data" / "registry.json"


# Define expected request format
class ValidationRequest(BaseModel):
    dataset_id: str


# Welcome endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to HDFC Custom LLM Pipeline API",
        "status": "running"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "dataset-governance-api"
    }


# Get demo dataset information
@app.get("/datasets/demo")
def get_demo_dataset():

    if not DATASET_PATH.exists():
        raise HTTPException(
            status_code=404,
            detail="Demo dataset not found"
        )

    import json

    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        dataset = json.load(file)

    return {
        "dataset_id": dataset["dataset_id"],
        "dataset_version": dataset["dataset_version"],
        "source": dataset["source"],
        "purpose": dataset["purpose"],
        "classification": dataset["classification"],
        "record_count": len(dataset["records"])
    }


# Validate demo dataset
@app.post("/datasets/validate")
def validate_demo_dataset(request: ValidationRequest):

    if request.dataset_id != "HDFC-DEMO-001":
        raise HTTPException(
            status_code=404,
            detail="Dataset ID not found in demo registry"
        )

    result = validate_dataset(DATASET_PATH)

    return {
        "dataset_id": request.dataset_id,
        "validation_status": (
            "PASSED" if result["valid"] else "FAILED"
        ),
        "record_count": result["record_count"],
        "errors": result["errors"]
    }

@app.get("/datasets/registry")
def get_dataset_registry():

    if not REGISTRY_PATH.exists():
        raise HTTPException(
            status_code=404,
            detail="Dataset registry not found"
        )

    import json

    with open(REGISTRY_PATH, "r", encoding="utf-8") as file:
        registry = json.load(file)

    return registry

