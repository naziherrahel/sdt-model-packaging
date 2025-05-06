import cv2
import streamlit as st
from ultralytics import YOLO
from config import Settings

def main():
    settings = Settings()

    st.title("YOLOv8 Live Object Detection")
    model_variant = st.sidebar.selectbox(
        "Model Variant", ["yolov8n", "yolov8s", "yolov8m"], index=["yolov8n", "yolov8s", "yolov8m"].index(settings.model_name)
    )
    confidence = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, settings.confidence)
    run = st.sidebar.button("Start Detection")

    if run:
        model = YOLO(f"{model_variant}.pt")
        cap = cv2.VideoCapture(settings.camera_id)
        placeholder = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to read from camera.")
                break

            results = model(frame, conf=confidence)[0]
            annotated = results.plot()
            placeholder.image(annotated, channels="BGR")

        cap.release()

if __name__ == "__main__":
    main()
