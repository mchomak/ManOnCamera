# собирает датасет из несколькиз разных файлов
# collects a dataset from several different files

import os
import shutil

RootDir="C:\\Users\\OKS5-18\\PycharmProjects\\MenOnCamera\\DataSet\\images\\AllRight\\"
files=os.listdir(RootDir)

for file in files:
    images=os.listdir(os.path.join(RootDir,file))
    for img in images:
        shutil.copyfile(os.path.join(RootDir,file,img),os.path.join(RootDir,"allimages",img))