import json
from pathlib import Path
from datetime import datetime
from uuid import uuid4

AUDIT_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "audit_log.json"
)

def load_audit_log():
    if not AUDIT_FILE.exists():
        return []

    with open(AUDIT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def log_event(dataset_id, action, details=""):
    logs = load_audit_log()

    event = {
        "event_id": str(uuid4()),
        "dataset_id": dataset_id,
        "action": action,
        "details": details,
        "performed_by": "demo_user",
        "timestamp": datetime.now().isoformat()
    }

    logs.append(event)

    AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(AUDIT_FILE, "w", encoding="utf-8") as file:
        json.dump(logs, file, indent=4)

    return event