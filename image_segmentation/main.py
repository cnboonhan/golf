from ultralytics import YOLO
import os

model = YOLO("yolo11n-seg.pt")
# model = YOLO("/home/bhn/workspaces/golf/runs/segment/train/weights/best.pt")
# model = YOLO("best.pt")

results = model.train(
    data=f"{os.getcwd()}/golf_train.yaml",
    epochs=10,
    pretrained=False,
    resume=False,
    device="cuda:1",
)

results = model(
    "./data/yolo/test/images/m2c_2275_jpg.rf.7885e14523a3379a57324505ba10b58f.jpg",
    save=True,
    show_boxes=True,
    exist_ok=True,
)
