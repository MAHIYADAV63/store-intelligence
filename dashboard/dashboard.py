import streamlit as st
import json
from collections import Counter

EVENT_FILE = "./data/events.jsonl"

st.title("Store Intelligence Dashboard")

counter = Counter()

try:

    with open(EVENT_FILE, "r") as f:

        for line in f:

            event = json.loads(line)

            counter[event["event_type"]] += 1

except Exception as e:

    st.error(str(e))

st.subheader("Analytics")

st.write(dict(counter))
