import json
from collections import Counter

counts = Counter()

with open("data/events.jsonl","r") as f:

    for line in f:

        event = json.loads(line)

        counts[event["event_type"]] += 1

print("\n===== STORE ANALYTICS =====\n")

for event,count in counts.items():
    print(f"{event}: {count}")

print("\n===========================\n")
