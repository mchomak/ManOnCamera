from ultralytics import YOLO
import os

RootDir=os.getcwd()

model = YOLO("yolov8x.yaml")  # build a new model from scratch
print(model.info())
results = model.train(data=os.path.join(RootDir, "config.yaml"), epochs=1)