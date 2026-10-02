from datetime import datetime
from src.registry_store import load_registry, save_registry
from src.audit_log import log_event


def update_dataset_status(dataset_id, new_status, reviewer="demo_reviewer"):

    registry = load_registry()

    for dataset in registry["datasets"]:

        if dataset["dataset_id"] == dataset_id:

            if new_status not in ["APPROVED", "REJECTED"]:
                raise ValueError("Invalid approval status.")

            dataset["status"] = new_status
            dataset["reviewed_by"] = reviewer
            dataset["reviewed_at"] = datetime.now().isoformat()

            save_registry(registry)

            log_event(
                dataset_id=dataset_id,
                action=f"DATASET_{new_status}",
                details=f"Dataset status changed to {new_status}"
            )

            return dataset

    raise ValueError("Dataset not found.")