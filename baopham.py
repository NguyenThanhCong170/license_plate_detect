import easyocr
import cv2
import os 
import csv

cap = cv2.imread('abc1.jpg')
reader = easyocr.Reader(['en'], gpu=True)

def read_license_plate(image):
    '''detections = reader.readtext(license_plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '-').replace('*',"-")'''
    #return text, score
    result = reader.readtext(image, detail = 0)
    output = "".join(result)
    output = output.upper().replace(' ',"-").replace('*',"-")
    return output

output= read_license_plate(cap)
print(output)
cv2.imshow('ab',cap)
cv2.waitKey(0)
filepath = r'C:\Users\phamq\OneDrive\Desktop\license_plate_detect\biensoxe.csv'
if not os.path.isfile(filepath):
    file = open('biensoxe.csv', 'w', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow([output])
    file.close()
else:
    file= open('biensoxe.csv', 'a', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow([output])
    file.close()