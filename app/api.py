from fastapi import FastAPI
import json
from collections import Counter

app = FastAPI()

EVENT_FILE = "./data/events.jsonl"


@app.get("/")
def home():
    return {"message": "Store Intelligence API Running"}


@app.get("/events")
def get_events():

    events = []

    try:
        with open(EVENT_FILE, "r") as f:
            for line in f:
                events.append(json.loads(line))

    except:
        pass

    return events


@app.get("/analytics")
def analytics():

    counter = Counter()

    try:
        with open(EVENT_FILE, "r") as f:

            for line in f:

                event = json.loads(line)

                counter[event["event_type"]] += 1

    except:
        pass

    return dict(counter)


@app.get("/health")
def health():
    return {"status":"healthy"}
