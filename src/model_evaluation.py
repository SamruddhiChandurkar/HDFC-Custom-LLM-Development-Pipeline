import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

EVALUATION_FILE = (
    PROJECT_ROOT
    / "data"
    / "evaluation_dataset.json"
)

REPORT_FILE = (
    PROJECT_ROOT
    / "data"
    / "evaluation_report.json"
)


def load_dataset():

    with open(
        EVALUATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def evaluate_routes():

    from src.agent import BankingAgent

    agent = BankingAgent()

    dataset = load_dataset()

    results = []

    passed = 0

    for item in dataset:

        response = agent.ask(
            item["question"]
        )

        actual = response.get(
            "route"
        )

        expected = item[
            "expected_route"
        ]

        success = (
            actual == expected
        )

        if success:
            passed += 1

        results.append({
            "id": item["id"],
            "expected": expected,
            "actual": actual,
            "passed": success
        })

    total = len(dataset)

    report = {
        "model_version": "v1",
        "evaluation_type": "agent_routing",
        "total": total,
        "passed": passed,
        "failed": total - passed,
        "accuracy": (
            passed / total
            if total
            else 0
        ),
        "results": results
    }

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return report


if __name__ == "__main__":

    print(
        json.dumps(
            evaluate_routes(),
            indent=4
        )
    )