import os

path="C:\\Users\\OKS5-18\\PycharmProjects\\MenOnCamera\\DataSet\\images\\Nothing\\Egor2"

files = os.listdir(path=path)
print(len(files))

num=1
for i in files:
    os.rename(path+"\\" + str(i), path+"\\" + "egor2_" + str(num)+".jpg")

    num+=1