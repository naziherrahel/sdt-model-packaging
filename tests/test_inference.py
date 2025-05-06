import numpy as np
from ultralytics import YOLO

def test_model_smoke():
    model = YOLO("yolov8n.pt")
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    results = model(img, conf=0.3)[0]
    assert hasattr(results, "boxes")
