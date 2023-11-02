from ultralytics import YOLO
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="data_settings.yaml", epochs=1)  # train the model
