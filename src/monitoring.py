import json
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MONITORING_FILE = (
    PROJECT_ROOT
    / "data"
    / "monitoring.json"
)


def load_metrics():

    if not MONITORING_FILE.exists():

        return {
            "requests": 0,
            "errors": 0,
            "safety_blocks": 0,
            "routes": {},
            "last_updated": None
        }

    with open(
        MONITORING_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def record_request(
    route,
    error=False,
    safety_block=False
):

    metrics = load_metrics()

    metrics["requests"] += 1

    if error:
        metrics["errors"] += 1

    if safety_block:
        metrics["safety_blocks"] += 1

    metrics["routes"][route] = (
        metrics["routes"].get(route, 0)
        + 1
    )

    metrics["last_updated"] = (
        datetime.now().isoformat()
    )

    MONITORING_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        MONITORING_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4
        )

    return metrics