# удаляет ненужные кадры
# removes unnecessary frames

import os

path="C:\\Users\\OKS5-18\\PycharmProjects\\MenOnCamera\\DataSet\\images\\Nothing\\Egor2"
files = os.listdir(path=path)
print(len(files))

num=1
def Deliter(path,k):
    files = os.listdir(path)
    num = 1
    for i in files:
        if num % k == 0:
            pass
        else:
            os.remove(path+"\\"+str(i))

        num += 1