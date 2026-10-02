import json
from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parent.parent

AUDIT_LOG_PATH = PROJECT_ROOT / "data" / "audit_log.json"


class AuditLogger:

    def __init__(self, log_path=None):

        if log_path is None:
            self.log_path = AUDIT_LOG_PATH
        else:
            self.log_path = Path(log_path)

        self.log_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.log_path.exists():

            with open(
                self.log_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump([], file, indent=4)


    def load_logs(self):

        if not self.log_path.exists():
            return []

        with open(
            self.log_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    def save_logs(self, logs):

        with open(
            self.log_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                logs,
                file,
                indent=4
            )


    def log_event(
        self,
        event_type,
        dataset_name,
        dataset_version,
        details=None
    ):

        logs = self.load_logs()

        event = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "dataset_name": dataset_name,
            "dataset_version": dataset_version,
            "details": details or {}
        }

        logs.append(event)

        self.save_logs(logs)

        return event


    def get_dataset_history(self, dataset_name):

        logs = self.load_logs()

        history = []

        for event in logs:

            if event.get("dataset_name") == dataset_name:

                history.append(event)

        return history
    def get_history(self):
        return self.load_logs()
    
    


# ---------------------------------------------------------
# Backward-compatible helper functions
# ---------------------------------------------------------

def load_audit_log():

    logger = AuditLogger()

    return logger.load_logs()


def log_event(
    dataset_id,
    action,
    details
):

    logger = AuditLogger()

    return logger.log_event(
        event_type=action,
        dataset_name=dataset_id,
        dataset_version="unknown",
        details={
            "message": details
        }
    )
def get_history(self):
    return self.load_logs()