import cv2
import numpy as np
from matplotlib import pyplot as plt

#cv2.cvtColor(input_image, flag)
#flag =>  cv2.COLOR_BGR2GRAY  (BGR -> Gray)
#flag =>  cv2.COLOR_BGR2HSV  (BGR -> HSV)    #HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]



img = cv2.imread('C://Users//alsaifyt//Desktop//PythonOpenCvScripts//gradient.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]






for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()