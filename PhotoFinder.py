import os

image_path="C:\\Users\\OKS5-18\\PycharmProjects\\MenOnCamera\\DataSet\\Result\\"
label_path="C:\\Users\\OKS5-18\\PycharmProjects\\MenOnCamera\\DataSet\\RGtest3-20230320T151005Z-001\\RGtest3\\"
label_files = os.listdir(label_path)
print(len(label_path))

image_files = os.listdir(image_path)
print(len(image_files))

missing_files=[]

for image in label_files:
    if (image[:-4]+".jpg") not in image_files:
        os.remove(image_path + "\\" + image[:-4] + ".jpg")
#         missing_files.append((image[:-4]+".jpg"))
#
# print(missing_files)
# print(len(missing_files))
#
# for i in missing_files:
#     os.remove(image_path+"\\"+i[:-4]+".jpg")