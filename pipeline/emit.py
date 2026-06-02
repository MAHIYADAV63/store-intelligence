import json
from uuid import uuid4
from datetime import datetime

OUTPUT_FILE = "data/events.jsonl"

def emit_event(
        store_id,
        camera_id,
        visitor_id,
        event_type,
        zone_id=None,
        confidence=0.9):

    event = {

        "event_id":str(uuid4()),
        "store_id":store_id,
        "camera_id":camera_id,
        "visitor_id":str(visitor_id),
        "event_type":event_type,
        "timestamp":datetime.utcnow().isoformat(),
        "zone_id":zone_id,
        "confidence":confidence
    }

    with open(OUTPUT_FILE,"a") as f:
        f.write(json.dumps(event)+"\n")

    print(event)
