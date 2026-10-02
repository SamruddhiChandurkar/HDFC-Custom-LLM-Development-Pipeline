from pathlib import Path
import json

from fastapi import (
    FastAPI,
    HTTPException,
    UploadFile,
    File
)

from pydantic import BaseModel

from src.data_validator import validate_dataset
from src.intake import register_dataset
from src.registry_store import (
    load_registry,
    add_dataset
)
from src.audit_log import (
    load_audit_log,
    log_event
)
from src.approval import (
    update_dataset_status
)

from loan_assistant import LoanAssistant

from src.calculator import calculate_emi
from src.agent import BankingAgent

from src.model_registry import (
    load_models,
    register_model
)

from src.monitoring import load_metrics

from src.pdf_assistant import PDFPolicyAssistant
from src.pdf_rag import PDFPolicyRAG


# ============================================================
# CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="HDFC Custom LLM Pipeline API",
    description=(
        "Agentic AI Banking Platform with "
        "RAG, Governance, Safety, Audit and "
        "Policy PDF Intelligence"
    ),
    version="1.0.0"
)


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = (
    Path(__file__).resolve().parent.parent
)

DATASET_PATH = (
    PROJECT_ROOT
    / "data"
    / "banking_records.json"
)

REGISTRY_PATH = (
    PROJECT_ROOT
    / "data"
    / "registry.json"
)


# ============================================================
# REQUEST MODELS
# ============================================================

class ValidationRequest(BaseModel):

    dataset_id: str


class DatasetIntakeRequest(BaseModel):

    dataset_id: str
    dataset_name: str
    purpose: str
    source: str
    classification: str
    version: str


class DatasetApprovalRequest(BaseModel):

    dataset_id: str
    status: str
    reviewer: str = "demo_reviewer"


class AssistantRequest(BaseModel):

    question: str


class EMIRequest(BaseModel):

    principal: float
    annual_rate: float
    months: int


class AgentRequest(BaseModel):

    question: str


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "message": (
            "Welcome to HDFC Custom "
            "LLM Pipeline API"
        ),
        "status": "running",
        "version": "1.0.0"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "hdfc-custom-llm-pipeline"
    }


# ============================================================
# DEMO DATASET
# ============================================================

@app.get("/datasets/demo")
def get_demo_dataset():

    if not DATASET_PATH.exists():

        raise HTTPException(
            status_code=404,
            detail="Demo dataset not found"
        )

    with open(
        DATASET_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        dataset = json.load(file)

    return {
        "dataset_id": dataset.get(
            "dataset_id"
        ),

        "dataset_version": dataset.get(
            "dataset_version"
        ),

        "source": dataset.get(
            "source"
        ),

        "purpose": dataset.get(
            "purpose"
        ),

        "classification": dataset.get(
            "classification"
        ),

        "record_count": len(
            dataset.get(
                "records",
                []
            )
        )
    }


# ============================================================
# DATASET VALIDATION
# ============================================================

@app.post("/datasets/validate")
def validate_dataset_endpoint(
    request: ValidationRequest
):

    if not DATASET_PATH.exists():

        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    with open(
        DATASET_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        dataset = json.load(file)

    if (
        dataset.get("dataset_id")
        != request.dataset_id
    ):

        raise HTTPException(
            status_code=404,
            detail="Dataset ID not found"
        )

    result = validate_dataset(
        dataset
    )

    log_event(
        dataset_id=request.dataset_id,
        action="DATASET_VALIDATED",
        details=(
            "Dataset validation completed."
        )
    )

    return result


# ============================================================
# DATASET INTAKE
# ============================================================

@app.post("/datasets/intake")
def dataset_intake(
    request: DatasetIntakeRequest
):

    try:

        result = register_dataset(

            dataset_id=request.dataset_id,

            dataset_name=request.dataset_name,

            purpose=request.purpose,

            source=request.source,

            classification=request.classification,

            version=request.version
        )

        registry = add_dataset(
            result
        )

        log_event(
            dataset_id=request.dataset_id,
            action="DATASET_REGISTERED",
            details=(
                "Dataset successfully added "
                "to persistent registry."
            )
        )

        return {

            "success": True,

            "message": (
                "Dataset registered successfully."
            ),

            "dataset": result,

            "total_registered_datasets":
                len(
                    registry["datasets"]
                )
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# DATASET REGISTRY
# ============================================================

@app.get("/datasets/registry")
def get_dataset_registry():

    return load_registry()


# ============================================================
# DATASET APPROVAL / REJECTION
# ============================================================

@app.post("/datasets/approve")
def approve_dataset(
    request: DatasetApprovalRequest
):

    try:

        result = update_dataset_status(

            dataset_id=request.dataset_id,

            new_status=request.status,

            reviewer=request.reviewer
        )

        return {

            "success": True,

            "message": (
                "Dataset review completed."
            ),

            "dataset": result
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# AUDIT LOGS
# ============================================================

@app.get("/audit/logs")
def get_audit_logs():

    logs = load_audit_log()

    return {

        "total_events": len(logs),

        "events": logs
    }


# ============================================================
# LOAN ASSISTANT
# ============================================================

@app.post("/assistant/ask")
def ask_assistant(
    request: AssistantRequest
):

    assistant = LoanAssistant()

    try:

        result = assistant.ask(
            request.question
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ============================================================
# AGENTIC AI
# ============================================================

@app.post("/v1/agent")
def agent_query(
    request: AgentRequest
):

    try:

        agent = BankingAgent()

        result = agent.ask(
            request.question
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ============================================================
# MAIN AI INFERENCE ENDPOINT
# ============================================================

@app.post("/v1/inference")
def inference(
    request: AssistantRequest
):

    try:

        agent = BankingAgent()

        result = agent.ask(
            request.question
        )

        return {

            "api_version": "v1",

            "model_version": "v1",

            "question": request.question,

            "answer": result.get(
                "answer"
            ),

            "route": result.get(
                "route",
                "UNKNOWN"
            ),

            "confidence": result.get(
                "confidence",
                "UNKNOWN"
            ),

            "sources": result.get(
                "sources",
                []
            ),

            "pii_detected": result.get(
                "pii_detected",
                False
            )
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ============================================================
# EMI CALCULATOR
# ============================================================

@app.post("/v1/emi")
def emi_endpoint(
    request: EMIRequest
):

    try:

        result = calculate_emi(

            principal=request.principal,

            annual_rate=request.annual_rate,

            months=request.months
        )

        log_event(

            dataset_id="CALCULATOR",

            action="EMI_CALCULATION",

            details=(
                "EMI calculation completed."
            )
        )

        return {

            "success": True,

            "result": result
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# MODEL REGISTRY
# ============================================================

@app.get("/v1/models")
def models_endpoint():

    return load_models()


# ============================================================
# REGISTER MODEL
# ============================================================

@app.post("/v1/models/register")
def register_model_endpoint(
    model: dict
):

    try:

        result = register_model(
            model
        )

        return {

            "success": True,

            "model": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# ============================================================
# MONITORING
# ============================================================

@app.get("/v1/monitoring")
def monitoring_endpoint():

    return load_metrics()


# ============================================================
# POLICY PDF UPLOAD
# ============================================================

@app.post("/v1/policies/upload")
async def upload_policy(
    file: UploadFile = File(...)
):

    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="File name is required."
        )

    if not file.filename.lower().endswith(
        ".pdf"
    ):

        raise HTTPException(
            status_code=400,
            detail=(
                "Only PDF files are supported."
            )
        )

    rag = PDFPolicyRAG()

    try:

        result = rag.add_pdf(
            file
        )

        log_event(
            dataset_id="POLICY_PDF",
            action="POLICY_PDF_UPLOADED",
            details=(
                f"Policy PDF uploaded: "
                f"{file.filename}"
            )
        )

        return {

            "success": True,

            "message": (
                "Policy PDF uploaded and "
                "indexed successfully."
            ),

            "document": result
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=(
                "PDF processing failed: "
                f"{str(error)}"
            )
        )


# ============================================================
# POLICY PDF QUERY
# ============================================================

@app.post("/v1/policies/query")
def query_policy(
    request: AgentRequest
):

    try:

        assistant = PDFPolicyAssistant()

        result = assistant.ask(
            request.question
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# ============================================================
# LIST POLICY PDFs
# ============================================================

@app.get("/v1/policies")
def list_policies():

    try:

        rag = PDFPolicyRAG()

        documents = rag.get_documents()

        return {

            "total_documents": len(
                documents
            ),

            "documents": documents
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )