from ultralytics import YOLO
import cv2
import time

from pipeline.config import STORE_ID
from pipeline.emit import emit_event

model = YOLO("yolov8n.pt")

VIDEO = "data/CAM 5.mp4"

# BILLING COUNTER ZONE
ZONE_X1 = 220
ZONE_Y1 = 70
ZONE_X2 = 610
ZONE_Y2 = 650

inside = set()
last_event_time = {}

COOLDOWN_SECONDS = 30

results = model.track(
    source=VIDEO,
    tracker="bytetrack.yaml",
    persist=True,
    classes=[0],
    conf=0.45,
    stream=True
)

for r in results:

    frame = r.orig_img

    cv2.rectangle(
        frame,
        (ZONE_X1, ZONE_Y1),
        (ZONE_X2, ZONE_Y2),
        (0,255,0),
        3
    )

    if r.boxes.id is not None:

        ids = r.boxes.id.int().cpu().tolist()
        boxes = r.boxes.xyxy.cpu().tolist()

        for box, track_id in zip(boxes, ids):

            x1,y1,x2,y2 = map(int, box)

            width = x2-x1
            height = y2-y1

            # Ignore tiny detections
            if width < 60 or height < 120:
                continue

            cx = (x1+x2)//2
            cy = (y1+y2)//2

            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

            in_zone = (
                ZONE_X1 <= cx <= ZONE_X2 and
                ZONE_Y1 <= cy <= ZONE_Y2
            )

            current_time = time.time()

            if track_id not in last_event_time:
                last_event_time[track_id] = 0

            # ENTER
            if in_zone and track_id not in inside:

                if current_time-last_event_time[track_id] > COOLDOWN_SECONDS:

                    inside.add(track_id)
                    last_event_time[track_id]=current_time

                    emit_event(
                        STORE_ID,
                        "CAM5",
                        track_id,
                        "BILLING_QUEUE_ENTER"
                    )

            # EXIT
            elif not in_zone and track_id in inside:

                if current_time-last_event_time[track_id] > COOLDOWN_SECONDS:

                    inside.remove(track_id)
                    last_event_time[track_id]=current_time

                    emit_event(
                        STORE_ID,
                        "CAM5",
                        track_id,
                        "BILLING_QUEUE_EXIT"
                    )

    cv2.imshow("CAM5 BILLING", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
