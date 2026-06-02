from ultralytics import YOLO
import cv2

from pipeline.config import STORE_ID
from pipeline.emit import emit_event

model = YOLO("yolov8n.pt")

VIDEO = "data/CAM 3.mp4"

ENTRY_LINE = 500

seen = {}

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
        (ENTRY_LINE,0),
        (ENTRY_LINE,1080),
        (0,255,0),
        3
    )

    if r.boxes.id is not None:

        ids = r.boxes.id.int().cpu().tolist()
        boxes = r.boxes.xyxy.cpu().tolist()

        for box, track_id in zip(boxes, ids):

            x1,y1,x2,y2 = map(int,box)

            cx = (x1+x2)//2
            cy = (y1+y2)//2

            cv2.circle(
                frame,
                (cx,cy),
                5,
                (0,0,255),
                -1
            )

            if track_id in seen:

                old_x = seen[track_id]

                if old_x < ENTRY_LINE and cx >= ENTRY_LINE:

                    emit_event(
                        STORE_ID,
                        "CAM3",
                        track_id,
                        "ENTRY"
                    )

                elif old_x > ENTRY_LINE and cx <= ENTRY_LINE:

                    emit_event(
                        STORE_ID,
                        "CAM3",
                        track_id,
                        "EXIT"
                    )

            seen[track_id] = cx

    cv2.imshow("CAM3 ENTRY", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
