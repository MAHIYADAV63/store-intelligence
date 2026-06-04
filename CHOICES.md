# CHOICES.md

# Engineering Decisions

## Model Selection

### YOLOv8

Chosen because:

* Fast inference
* High detection accuracy
* Easy deployment
* Strong OpenCV integration

## Tracking Selection

### ByteTrack

Chosen because:

* Robust multi-object tracking
* Stable identity preservation
* Works well with CCTV footage

## Event Schema Design

JSONL event schema:

* event_id
* store_id
* camera_id
* visitor_id
* event_type
* timestamp
* zone_id
* confidence

Benefits:

* Streaming-friendly
* Easy analytics processing
* Human readable

## API Architecture

FastAPI was selected because:

* High performance
* Automatic Swagger documentation
* Easy deployment
* Production-ready

## Analytics Strategy

Events are aggregated from JSONL files and exposed through APIs and dashboards.

## Deployment Choice

Render was selected for:

* Fast deployment
* Public API access
* Free hosting tier
* Easy GitHub integration

