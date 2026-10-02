import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEPLOYMENT_FILE = (
    PROJECT_ROOT
    / "data"
    / "deployment_registry.json"
)


def load_deployment():

    with open(
        DEPLOYMENT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def activate_version(version):

    data = load_deployment()

    found = False

    for item in data["versions"]:

        if item["version"] == version:

            item["status"] = "ACTIVE"
            item["traffic_percentage"] = 100

            found = True

        else:

            item["status"] = "INACTIVE"
            item["traffic_percentage"] = 0

    if not found:

        raise ValueError(
            f"Model version '{version}' not found."
        )

    data["active_version"] = version

    with open(
        DEPLOYMENT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    return data
