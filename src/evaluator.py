import json
from pathlib import Path

from src.agent import BankingAgent


PROJECT_ROOT = Path(__file__).resolve().parent.parent

EVAL_FILE = (
    PROJECT_ROOT
    / "data"
    / "evaluation_dataset.json"
)


def load_evaluation_dataset():

    with open(
        EVAL_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def run_evaluation():

    agent = BankingAgent()

    dataset = load_evaluation_dataset()

    results = []

    correct = 0

    for item in dataset:

        response = agent.ask(
            item["question"]
        )

        actual_route = response.get(
            "route"
        )

        passed = (
            actual_route
            == item["expected_route"]
        )

        if passed:
            correct += 1

        results.append(
            {
                "id": item["id"],
                "question": item["question"],
                "expected_route":
                    item["expected_route"],
                "actual_route":
                    actual_route,
                "passed": passed
            }
        )

    total = len(dataset)

    accuracy = (
        correct / total
        if total
        else 0
    )

    return {
        "total_tests": total,
        "passed": correct,
        "failed": total - correct,
        "route_accuracy": round(
            accuracy,
            4
        ),
        "results": results
    }


if __name__ == "__main__":

    result = run_evaluation()

    print(
        json.dumps(
            result,
            indent=4
        )
    )