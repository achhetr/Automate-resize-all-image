import cv2
import os

folder_path = os.getcwd()

list_1 = os.listdir(folder_path + "/sample-images")

for l in list_1:
    img = cv2.imread("sample-images/" + l ,1)
    img2 = cv2.resize(img,(100,100))
    cv2.imwrite("output-images/" + l,img2)
print("SUCESS!")
