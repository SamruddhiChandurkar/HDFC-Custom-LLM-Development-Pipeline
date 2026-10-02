import json
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_REGISTRY_PATH = (
    PROJECT_ROOT
    / "data"
    / "model_registry.json"
)


def load_models():

    if not MODEL_REGISTRY_PATH.exists():

        return {
            "models": []
        }

    with open(
        MODEL_REGISTRY_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_models(data):

    MODEL_REGISTRY_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        MODEL_REGISTRY_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def register_model(
    model_id,
    version,
    base_model,
    adapter=None,
    status="EVALUATION"
):

    registry = load_models()

    model = {

        "model_id": model_id,

        "version": version,

        "base_model": base_model,

        "adapter": adapter,

        "status": status,

        "registered_at":
            datetime.now().isoformat()

    }

    registry["models"].append(model)

    save_models(registry)

    return model