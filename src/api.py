
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.data_validator import validate_dataset
from pydantic import BaseModel
from src.intake import register_dataset
from src.registry_store import load_registry, add_dataset
from src.audit_log import load_audit_log, log_event
from src.approval import update_dataset_status

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

class DatasetApprovalRequest(BaseModel):
    dataset_id: str
    status: str
    reviewer: str = "demo_reviewer"


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
@app.post("/datasets/intake")
def dataset_intake(request: DatasetIntakeRequest):
    try:
        result = register_dataset(
            dataset_id=request.dataset_id,
            dataset_name=request.dataset_name,
            purpose=request.purpose,
            source=request.source,
            classification=request.classification,
            version=request.version
        )

        registry = add_dataset(result)

        return {
            "message": "Dataset registered successfully.",
            "dataset": result,
            "total_registered_datasets": len(registry["datasets"])
        }

    except ValueError as error:
        return {
            "message": "Dataset registration failed.",
            "error": str(error)
        }

@app.get("/datasets/registry")
def get_dataset_registry():
    return load_registry()


@app.post("/datasets/intake")
def dataset_intake(request: DatasetIntakeRequest):
    try:
        result = register_dataset(
            dataset_id=request.dataset_id,
            dataset_name=request.dataset_name,
            purpose=request.purpose,
            source=request.source,
            classification=request.classification,
            version=request.version
        )

        registry = add_dataset(result)

        log_event(
            dataset_id=request.dataset_id,
            action="DATASET_REGISTERED",
            details="Dataset successfully added to persistent registry"
        )

        return {
            "message": "Dataset registered successfully.",
            "dataset": result,
            "total_registered_datasets": len(registry["datasets"])
        }

    except ValueError as error:
        return {
            "message": "Dataset registration failed.",
            "error": str(error)
        }
    

@app.get("/audit/logs")
def get_audit_logs():
    logs = load_audit_log()

    return {
        "total_events": len(logs),
        "events": logs
    }
@app.post("/datasets/approve")
def approve_dataset(request: DatasetApprovalRequest):

    try:
        result = update_dataset_status(
            dataset_id=request.dataset_id,
            new_status=request.status,
            reviewer=request.reviewer
        )

        return {
            "message": "Dataset review completed.",
            "dataset": result
        }

    except ValueError as error:
        return {
            "message": "Dataset review failed.",
            "error": str(error)
        }