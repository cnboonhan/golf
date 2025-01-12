from ultralytics import YOLO

model = YOLO("best.pt")
VIDEO_PATH = "./data/golf.mp4"

results = model(VIDEO_PATH, save=True)
