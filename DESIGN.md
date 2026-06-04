# DESIGN.md

# Store Intelligence System Design

## Overview

The Store Intelligence System processes multi-camera CCTV footage and converts raw video streams into actionable retail analytics.

The system performs:

* Person Detection
* Multi-Object Tracking
* Zone Intelligence
* Event Streaming
* Analytics
* Anomaly Detection
* API Serving

## Architecture

CCTV Cameras

↓

YOLOv8 Detection

↓

ByteTrack Tracking

↓

Zone Analytics Engine

↓

Event Generation (JSONL)

↓

Analytics Layer

↓

FastAPI APIs

↓

Streamlit Dashboard

## Components

### Detection Layer

YOLOv8 is used for person detection.

### Tracking Layer

ByteTrack maintains visitor identities across frames.

### Event Layer

Events are generated whenever visitors enter or exit predefined zones.

### Analytics Layer

Aggregates event counts and visitor activity.

### API Layer

FastAPI exposes event and analytics endpoints.

### Dashboard Layer

Streamlit visualizes store intelligence metrics.

## AI-Assisted Decisions

AI tools were used to evaluate:

* Detection model choices
* Tracking approaches
* Event schema design
* API structure
* Deployment workflow

Final engineering decisions were validated through implementation and testing.

