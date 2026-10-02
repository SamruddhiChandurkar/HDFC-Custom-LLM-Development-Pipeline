import json
from src.audit_log import AuditLogger


def test_audit_logger_creates_log(tmp_path):

    log_file = tmp_path / "audit_log.json"

    logger = AuditLogger(str(log_file))

    event = logger.log_event(
        event_type="DATASET_REGISTERED",
        dataset_name="test_dataset.csv",
        dataset_version="v1",
        details={
            "records": 100,
            "source": "test"
        }
    )

    assert event["event_type"] == "DATASET_REGISTERED"
    assert event["dataset_name"] == "test_dataset.csv"

    history = logger.get_history()

    assert len(history) == 1
    assert history[0]["dataset_name"] == "test_dataset.csv"


def test_dataset_history(tmp_path):

    log_file = tmp_path / "audit_log.json"

    logger = AuditLogger(str(log_file))

    logger.log_event(
        "DATASET_REGISTERED",
        "loan.csv",
        "v1"
    )

    logger.log_event(
        "DATASET_VALIDATED",
        "loan.csv",
        "v1"
    )

    history = logger.get_dataset_history("loan.csv")

    assert len(history) == 2
    assert history[0]["event_type"] == "DATASET_REGISTERED"
    assert history[1]["event_type"] == "DATASET_VALIDATED"