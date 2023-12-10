from ultralytics import YOLO
import cv2
import math
import random
from OCR import OCR_va_CSV
import pandas as pd
import csv
import os

cap = cv2.imread('test_cuc_manh.jpg')
model = YOLO('runs/detect/train/weights/last.pt')
result = model('test_cuc_manh.jpg', show=True)
tap_hinhanhbicat = []
for r in result:
  boxes = r.boxes
  for box in boxes:
    x1, y1, x2, y2 = box.xyxy[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    print(x1, y1, x2, y2)

    conf = math.ceil((box.conf[0] * 100)) / 100
    print(conf)

    img_bicat = cap[y1:y2, x1:x2]
    tap_hinhanhbicat.append(img_bicat)
for i in tap_hinhanhbicat:
  OCR_va_CSV(i)
