
from fastapi.testclient import TestClient

from src.api import app


client = TestClient(app)


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_demo_dataset_endpoint():

    response = client.get("/datasets/demo")

    assert response.status_code == 200

    data = response.json()

    assert data["dataset_id"] == "HDFC-DEMO-001"
    assert data["record_count"] == 3


def test_registry_endpoint():

    response = client.get("/datasets/registry")

    assert response.status_code == 200

    data = response.json()

    assert data["registry_name"] == "HDFC Demo Dataset Registry"


def test_unknown_dataset_returns_404():

    response = client.post(
        "/datasets/validate",
        json={"dataset_id": "UNKNOWN-999"}
    )

    assert response.status_code == 404
