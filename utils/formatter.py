import json
import uuid
from datetime import datetime, timezone

def build_json_payload(target_name: str, status: str) -> str:
    """Builds a standardized JSON payload for API transmission."""
    payload_dict = {
        "transaction_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "target": target_name,
        "metrics": {
            "status": status,
            "processed_items": 0,
            "error_rate": 0.0
        }
    }
    return json.dumps(payload_dict, indent=2)
