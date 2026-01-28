from ultralytics import YOLO

# Use your trained model
model = YOLO("runs/detect/train7/weights/best.pt")  


model.predict(
    source="dataset/images/train",
    conf=0.001,      # VERY VERY LOW confidence
    iou=0.1,         # allow loose overlap
    max_det=50,
    save=True,
    show=True
)
