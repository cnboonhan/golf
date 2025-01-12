from ultralytics import YOLO

model = YOLO("yolo11n-seg.pt")

# try to predict
results = model(
    "./data/yolo/test/images/m2c_909_jpg.rf.20d754056ce1f9c2510f80dab1504bcb.jpg",
    save=True,
    show_boxes=True,
    exist_ok=True,
)

results = model.train(data="./golf_train.yaml", epochs=10, imgsz=640)
