from ultralytics import YOLO
import cv2
import math
import random
from OCR import doc_chu_cai
import pandas as pd
import csv
import os

cap = cv2.imread('test_cuc_manh.jpg')
model = YOLO('runs/detect/train/weights/last.pt')
result = model('test_cuc_manh.jpg', show = True)
tap_hinhanhbicat = []
for r in result:
    boxes = r.boxes
    for box in boxes:
        x1 ,y1,x2,y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int (y1), int (x2), int(y2)
        print(x1,y1,x2,y2)
       
            
        conf= math.ceil((box.conf[0]*100))/100
        print(conf)


        img_bicat = cap[y1:y2,x1:x2]
        tap_hinhanhbicat.append(img_bicat)
        
        
# for m in hinhanhbicat: #show cac hinh anh bi cat
#     a = random.randint(1,10000)
#     cv2.imshow(f'{a}',m)
tap_hinhanhbicat_chinhthuc = []

# khi nao can thi lay

'''for i in tap_hinhanhbicat: 
    hinhanhbicat_gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    _, hinhanhbicat_chinhthuc = cv2.threshold(hinhanhbicat_gray, 127,255, cv2.THRESH_BINARY_INV)
    tap_hinhanhbicat_chinhthuc.append(hinhanhbicat_chinhthuc)
for i in tap_hinhanhbicat_chinhthuc:
    chucai_biensoxe, dochinhxac_chucai = doc_chu_cai(i) 
    print(chucai_biensoxe)


cv2.waitKey(0)'''
def OCR_va_CSV(image):
      reader = easyocr.Reader(['en'], gpu=False)
  result = reader.readtext(image, detail = 0)
  output = "".join(result)
  output = output.upper().replace(' ',"-").replace('*',"-")
  print(result)

filepath = ".\Biensoxe.csv"
if not os.path.isfile('Biensoxe.csv'):
    file = open('Biensoxe.csv', 'w', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow([f'result'])
    file.close()
else:
    file = open('detect.csv', 'a', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow([f'result'])
    file.close()

