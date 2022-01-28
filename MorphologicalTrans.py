import cv2
import numpy as np
from matplotlib import pyplot as plt




###############################Erosion#########################
# it erodes away the boundaries of foreground object


img = cv2.imread('C://Users//alsaifyt//Desktop//PythonOpenCvScripts//j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Erosed')
plt.xticks([]), plt.yticks([])
plt.show()


###############################Dilation#########################
#it increases the white region in the image or size of foreground object increases.
 # It is useful in removing noise 

dilation = cv2.dilate(img,kernel,iterations = 1)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('Dilated')
plt.xticks([]), plt.yticks([])
plt.show()



###############################Opening#########################
#erosion followed by dilation


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.show()


###############################Closing#########################
#Dilation followed by Erosion
#Useful in closing small holes inside the foreground objects, or small black points on the object.

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.show()


###############################Morphological Gradient#########################
# It is the difference between dilation and erosion of an image.


gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gradient),plt.title('Morphological Gradient')
plt.xticks([]), plt.yticks([])
plt.show()


###############################Top Hat#########################
# It is the difference between input image and Opening of the image

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


###############################black Hat#########################
#he difference between the closing of the input image and input image.

blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)






