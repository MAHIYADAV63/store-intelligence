from ultralytics import YOLO
import cv2
import time

from pipeline.config import STORE_ID
from pipeline.emit import emit_event

model = YOLO("yolov8n.pt")

VIDEO = "data/CAM 3.mp4"

LINE_Y = 350

entered = set()
exited = set()

results = model.track(
    source=VIDEO,
    tracker="bytetrack.yaml",
    persist=True,
    classes=[0],
    stream=True
)

for r in results:

    frame = r.orig_img

    cv2.line(
        frame,
        (0, LINE_Y),
        (1400, LINE_Y),
        (0,255,0),
        3
    )

    if r.boxes.id is not None:

        ids = r.boxes.id.int().cpu().tolist()
        boxes = r.boxes.xyxy.cpu().tolist()

        for box, track_id in zip(boxes, ids):

            x1,y1,x2,y2 = map(int, box)

            cx = (x1+x2)//2
            cy = (y1+y2)//2

            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

            if cy < LINE_Y:

                if track_id not in entered:

                    entered.add(track_id)

                    emit_event(
                        STORE_ID,
                        "CAM3",
                        track_id,
                        "STORE_ENTRY"
                    )

            elif cy > LINE_Y:

                if track_id not in exited:

                    exited.add(track_id)

                    emit_event(
                        STORE_ID,
                        "CAM3",
                        track_id,
                        "STORE_EXIT"
                    )

    cv2.imshow("CAM3 ENTRY EXIT", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
