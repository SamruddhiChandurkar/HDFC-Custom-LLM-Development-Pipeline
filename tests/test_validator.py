
import json

from src.data_validator import validate_dataset


def create_valid_dataset(tmp_path):

    dataset = {
        "dataset_id": "TEST-001",
        "dataset_version": "1.0",
        "source": "Synthetic Test Data",
        "owner": "Test Team",
        "purpose": "internal_knowledge_classification",
        "classification": "internal_demo",
        "permission_status": "approved_for_demo",
        "deidentified": True,
        "records": [
            {
                "record_id": "REC-001",
                "text": "A savings account stores money.",
                "label": "account_information"
            }
        ]
    }

    file_path = tmp_path / "test_dataset.json"

    file_path.write_text(
        json.dumps(dataset),
        encoding="utf-8"
    )

    return file_path


def test_valid_dataset_passes(tmp_path):

    file_path = create_valid_dataset(tmp_path)

    result = validate_dataset(file_path)

    assert result["valid"] is True
    assert result["record_count"] == 1


def test_missing_file_fails(tmp_path):

    file_path = tmp_path / "missing.json"

    result = validate_dataset(file_path)

    assert result["valid"] is False
    assert "Dataset file does not exist." in result["errors"]


def test_unapproved_dataset_fails(tmp_path):

    file_path = create_valid_dataset(tmp_path)

    dataset = json.loads(file_path.read_text(encoding="utf-8"))

    dataset["permission_status"] = "pending"

    file_path.write_text(
        json.dumps(dataset),
        encoding="utf-8"
    )

    result = validate_dataset(file_path)

    assert result["valid"] is False
    assert "Dataset is not approved for this demo." in result["errors"]


def test_missing_record_text_fails(tmp_path):

    file_path = create_valid_dataset(tmp_path)

    dataset = json.loads(file_path.read_text(encoding="utf-8"))

    del dataset["records"][0]["text"]

    file_path.write_text(
        json.dumps(dataset),
        encoding="utf-8"
    )

    result = validate_dataset(file_path)

    assert result["valid"] is False
    assert "Record 1 is missing text." in result["errors"]


def test_invalid_json_fails(tmp_path):

    file_path = tmp_path / "invalid.json"

    file_path.write_text(
        "{ invalid json }",
        encoding="utf-8"
    )

    result = validate_dataset(file_path)

    assert result["valid"] is False
    assert "Invalid JSON format." in result["errors"]
