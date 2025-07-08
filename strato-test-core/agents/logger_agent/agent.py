import json
import os
from datetime import datetime
from .models import LogInput

LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "test_logs.jsonl")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_test_result(data: LogInput) -> dict:
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "test_name": data.test_name,
        "status": data.status,
        "logs": data.logs,
        "error": data.error,
        "screenshots": data.screenshots,
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return {"message": "Logged", "test_name": data.test_name} 