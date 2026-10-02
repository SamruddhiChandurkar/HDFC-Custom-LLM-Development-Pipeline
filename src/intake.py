from datetime import datetime


ALLOWED_CLASSIFICATIONS = {
    "PUBLIC",
    "INTERNAL",
    "CONFIDENTIAL",
    "RESTRICTED"
}


def register_dataset(
    dataset_id: str,
    dataset_name: str,
    purpose: str,
    source: str,
    classification: str,
    version: str
):
    classification = classification.upper()

    if classification not in ALLOWED_CLASSIFICATIONS:
        raise ValueError(
            f"Invalid classification: {classification}"
        )

    if not dataset_id.strip():
        raise ValueError("Dataset ID is required.")

    if not dataset_name.strip():
        raise ValueError("Dataset name is required.")

    if not purpose.strip():
        raise ValueError("Purpose is required.")

    if not source.strip():
        raise ValueError("Source is required.")

    if not version.strip():
        raise ValueError("Version is required.")

    return {
        "dataset_id": dataset_id,
        "dataset_name": dataset_name,
        "purpose": purpose,
        "source": source,
        "classification": classification,
        "version": version,
        "status": "REGISTERED",
        "registered_at": datetime.utcnow().isoformat()
    }