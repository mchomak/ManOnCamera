# подключение к камере и сохранение получаемых изображений
# connect to the camera and save the resulting images

import os
import cv2
import time

DELAY = 3 # Задержка в сек

## Wi-Fi камера rtsp://192.168.1.1
def save_pic(img_name,RootDir):
    vcap = cv2.VideoCapture('rtsp://192.168.1.1/MJPG')
    ret, frame = vcap.read()
    cv2.imwrite(f'{RootDir}\\images\\{img_name}.jpg', frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])

num = 1
while 1:
    save_pic(num,os.getcwd())
    num += 1
    time.sleep(DELAY)
