import json

EVENT_FILE = "./data/events.jsonl"

billing_count = 0
store_count = 0

with open(EVENT_FILE,"r") as f:

    for line in f:

        event = json.loads(line)

        if event["event_type"]=="BILLING_QUEUE_ENTER":
            billing_count += 1

        if event["event_type"]=="STORE_ENTRY":
            store_count += 1

print("\n===== ANOMALY REPORT =====\n")

if billing_count > 20:
    print("⚠️ High Billing Queue Detected")

if store_count > 50:
    print("⚠️ Heavy Store Traffic")

if billing_count == 0:
    print("⚠️ Billing Counter Inactive")

print("\n==========================")
