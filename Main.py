# получает изображение с камеры дрона, детектим людей и передаем данные через телеграм бота
# receives an image from the drone's camera, detects people and transmits data via telegram bot

from ultralytics import YOLO
import os
import cv2
import time
import TgBot
import ConectToCamera

RootDir=os.getcwd()
files=os.listdir(RootDir)

os.system('cmd /c "netsh" wlan connect name=iCam-H9R_003604')
time.sleep(3)
print('connect to camera')

if "images" not in files:
    os.makedirs(os.path.join(RootDir,"images"))

if "results" not in files:
    os.makedirs(os.path.join(RootDir,"results"))

model_path=os.path.join(RootDir, "model_300ep_2400ph.pt")
img_path=os.path.join(RootDir,"images")
files=os.listdir(os.path.join(RootDir,"images"))

kaef=0.4
DELAY = 1 # Задержка в секундах

ConectToCamera.save_pic(img_path,RootDir)

def MenDetection(img_name):
    image_data=[]
    model = YOLO(model_path)
    img = cv2.imread(os.path.join(img_path,img_name))
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #img=cv2.resize(img,(640,480))

    results = model(img)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(img, "MAN", (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2, cv2.LINE_AA)

        print(score)
        if score>=kaef:
            image_data.append(score)

    if len(image_data)>0:
        print(os.path.join(RootDir, "result", "R"+img_path))
        buf=cv2.imwrite(f"{RootDir}\\results\\R{img_name}", img)
        if buf:
            print("The photo is recognized")

        for i in image_data:
            TgBot.check_mans(i)

num = 1
while 1:
    ConectToCamera.save_pic(num,RootDir)
    MenDetection(f"{num}.jpg")
    num += 1
    time.sleep(DELAY)