from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")
results = model(
    "./data/test/m2c_909_jpg.rf.20d754056ce1f9c2510f80dab1504bcb.jpg",
    save=True,
    show_boxes=False,
    exist_ok=True,
)
