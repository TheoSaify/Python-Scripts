import cv2
import numpy as np


e1 = cv2.getTickCount()


img = cv2.imread('C://Users//alsaifyt//Desktop//PythonOpenCvScripts//imgColorC.png')


px = img[100,100]
print(px)     #[Bleu Green Red]

# accessing only blue pixel
print('Blue Values')
blue = img[100,100,0]
print(blue)

# accessing RED value
print('Red Values')
print(img.item(10,10,2))

# modifying RED value
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))

#returns a tuple of number of rows, columns and channels
print('rows , column, channels')
print(img.shape)

#Total number of pixels
print('Total number of Pixels')
print(img.size)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

print('time needed to execute')
print(time)