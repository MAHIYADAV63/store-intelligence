# Store Intelligence System

## Overview

AI-powered retail analytics system using CCTV cameras, YOLOv8, ByteTrack and OpenCV.

---

## Tech Stack

- Python
- YOLOv8
- ByteTrack
- OpenCV
- Docker

---

## Camera Mapping

### CAM1 — Skincare Zone
Events:
- SKINCARE_ZONE_ENTER
- SKINCARE_ZONE_EXIT

### CAM2 — Makeup Zone
Events:
- MAKEUP_ZONE_ENTER
- MAKEUP_ZONE_EXIT

### CAM3 — Entry / Exit
Events:
- STORE_ENTRY
- STORE_EXIT

### CAM4 — Storeroom
Events:
- STOREROOM_ENTER
- STOREROOM_EXIT

### CAM5 — Billing Counter
Events:
- BILLING_QUEUE_ENTER
- BILLING_QUEUE_EXIT

---

## Pipeline

Camera Feed

↓

YOLO Detection

↓

ByteTrack Tracking

↓

Zone Analytics

↓

emit_event()

↓

events.jsonl

↓

analytics.py

---

## Run Commands

Activate venv:

```bash
source venv/bin/activate
```

Run analytics:

```bash
python -m pipeline.analytics
```

Run cameras:

```bash
python -m pipeline.skincare
python -m pipeline.makeup
python -m pipeline.detect
python -m pipeline.storeroom
python -m pipeline.billing
```
## Features

- YOLOv8 person detection
- ByteTrack multi-object tracking
- Multi-camera retail analytics
- Zone intelligence
    - Skincare Zone
    - Makeup Zone
    - Billing Counter
    - Storeroom
- Event streaming using JSONL
- FastAPI production APIs
- Streamlit live dashboard
- Anomaly detection

---

## API

Run API server:

```bash
uvicorn app.api:app --reload
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Dashboard

Run dashboard:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```
---

## Architecture

Raw CCTV Videos

↓

YOLOv8 Person Detection

↓

ByteTrack Tracking

↓

Zone Logic + Event Detection

↓

JSON Event Stream (events.jsonl)

↓

Analytics Engine

↓

FastAPI APIs

↓

Streamlit Dashboard

↓

Anomaly Detection

---

## Anomaly Detection

Implemented anomaly monitoring:

- Billing Counter Inactive
- Low customer activity detection
- Event pattern monitoring

Run anomaly detector:

```bash
python -m pipeline.anomaly
```

---

## Production Readiness

- Modular pipeline architecture
- Event schema design
- Real-time API layer
- Dashboard monitoring
- Multi-camera support
- Docker support
- GitHub deployment ready

---

## Submission Notes

Dataset / CCTV videos are intentionally excluded from repository as per challenge instructions.
