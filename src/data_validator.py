
import json
from pathlib import Path


ALLOWED_PURPOSES = [
    "internal_knowledge_classification",
    "banking_terminology_normalization",
    "procedural_summarization",
    "templated_response_drafting"
]


def validate_dataset(file_path):

    file_path = Path(file_path)

    if not file_path.exists():
        return {
            "valid": False,
            "errors": ["Dataset file does not exist."]
        }

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            dataset = json.load(file)

    except json.JSONDecodeError:
        return {
            "valid": False,
            "errors": ["Invalid JSON format."]
        }

    errors = []

    required_fields = [
        "dataset_id",
        "dataset_version",
        "source",
        "owner",
        "purpose",
        "classification",
        "permission_status",
        "deidentified",
        "records"
    ]

    for field in required_fields:
        if field not in dataset:
            errors.append(f"Missing required field: {field}")

    if errors:
        return {
            "valid": False,
            "errors": errors
        }

    if dataset["purpose"] not in ALLOWED_PURPOSES:
        errors.append("Dataset purpose is not allowed.")

    if dataset["permission_status"] != "approved_for_demo":
        errors.append("Dataset is not approved for this demo.")

    if dataset["deidentified"] is not True:
        errors.append("Dataset is not marked as de-identified.")

    if not isinstance(dataset["records"], list):
        errors.append("Records must be a list.")

    else:
        for index, record in enumerate(dataset["records"]):

            if "record_id" not in record:
                errors.append(
                    f"Record {index + 1} is missing record_id."
                )

            if "text" not in record:
                errors.append(
                    f"Record {index + 1} is missing text."
                )

            if "label" not in record:
                errors.append(
                    f"Record {index + 1} is missing label."
                )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "dataset_id": dataset["dataset_id"],
        "record_count": len(dataset["records"])
        if isinstance(dataset["records"], list)
        else 0
    }
