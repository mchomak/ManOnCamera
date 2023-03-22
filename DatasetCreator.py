

from PIL import Image, ImageOps
import os
import cv2
import PhotoFinder
import PhotoDeliter
import PhotoRenemer

fileName=input()
RootDir="C:\\Users\\OKS5-18\\PycharmProjects\\MenOnCamera\\DataSet\\"
image_path=os.path.join(RootDir, "images", "Nothing", fileName)
os.makedirs(RootDir, exist_ok=True)

def FrameMaker(RootDir):
    video_path = f"{RootDir}\\Vidios\\{fileName}.mp4"
    cap = cv2.VideoCapture(video_path)
    print("video_path",video_path)

    ret, frame = cap.read()
    files=os.listdir(os.path.join(RootDir, "images", "Nothing"))
    if fileName not in files:
        os.makedirs(image_path)
    num = 0

    while ret:
        buf = cv2.imwrite(f"{RootDir}images\\Nothing\\{fileName}\\{num}.jpg", frame)
        ret, frame = cap.read()
        num += 1

    print("img_path",f"{RootDir}images\\Nothing\\{fileName}\\{num}.jpg")

def Deliter(path,k):
    files = os.listdir(path)
    num = 1
    for i in files:
        if num % k == 0:
            pass
        else:
            os.remove(path+"\\"+str(i))

        num += 1

def Renemer(path,k):
    files = os.listdir(path)

    num = 1
    for i in files:
        os.rename(f"{path}\\{str(i)}", path + f"\\Egor{k}_{str(num)}.jpg")

        num += 1

# отражаем изоброжение чтобы получить новое
def mirror(path_to_origin, img_name, output_folder):
    im = Image.open(path_to_origin + img_name)
    ImageOps.mirror(im).save(output_folder + "Mir" + img_name, "JPEG")

FrameMaker(RootDir)
Deliter(image_path,2)
Deliter(image_path,2)
Deliter(image_path,2)
Renemer(image_path,fileName[-1:])

img_names = os.listdir(image_path)

for img in img_names:
    if img[-4:]==".jpg":
        mirror(image_path+"\\", img, image_path+"\\")