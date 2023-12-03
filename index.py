from ultralytics import YOLO
import cv2

xe_model = YOLO('yolov8n.pt')

vehicles= [2,3,5,7]
cap= cv2.VideoCapture('bike_counter_10min.mp4')
frame_num=-1
ret=True
while ret and frame_num <10:
    frame_num +=1
    ret, frame = cap.read()
    if ret:
        detections= xe_model(frame)[0]
        detection_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, id= detection
            if int(id) in vehicles :
                detection_.append([x1,y1,x2,y2,score])
        
        
        

