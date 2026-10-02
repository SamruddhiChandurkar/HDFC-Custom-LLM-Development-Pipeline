
import json
from pathlib import Path


REGISTRY_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "registry.json"
)


def load_registry():
    """Read registered datasets from the JSON file."""

    if not REGISTRY_FILE.exists():
        return {
            "registry_name": "HDFC Demo Dataset Registry",
            "registry_version": "1.0",
            "datasets": []
        }

    with open(REGISTRY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_registry(registry):
    """Save the registry to the JSON file."""

    REGISTRY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(REGISTRY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            registry,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_dataset(dataset):
    """Add a new dataset and persist it."""

    registry = load_registry()

    for existing_dataset in registry["datasets"]:
        if existing_dataset["dataset_id"] == dataset["dataset_id"]:
            raise ValueError(
                "Dataset ID already exists in registry."
            )

    registry["datasets"].append(dataset)

    save_registry(registry)

    return registry
