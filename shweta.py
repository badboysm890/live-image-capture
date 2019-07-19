import face_recognition
import cv2
import time

video_capture = cv2.VideoCapture(0)
currentframe = 0
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    if  face_locations==[]:
        print("no")
    else: 
        name = 'frame' + str(currentframe) + '.png'
        print ('pic' + name) 
        cv2.imwrite(name, frame) 
        time.sleep(5)
        currentframe += 1
    