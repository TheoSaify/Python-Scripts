 # A LPF (low-pass filters) helps in removing noise, or blurring the image. A HPF filters helps in finding edges in an image.
import cv2
import numpy as np
from matplotlib import pyplot as plt


###############################2D Convolution ( Image Filtering )#########################
#for each pixel, a 5x5 window is centered on this pixel, all pixels falling within this window are summed up,
#and the result is then divided by 25. This equates to computing the average of the pixel values inside that window.


img = cv2.imread('C://Users//alsaifyt//Desktop//PythonOpenCvScripts//dave.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


###############################Image Blurring (Image Smoothing)#########################
#Image blurring is achieved by convolving the image with a low-pass filter kernel.
#It actually removes high frequency content (e.g: noise, edges) from the image 

#Method 1- Averaging
# This is done by convolving the image with a normalized box filter. 
# It simply takes the average of all the pixels under kernel area and replaces the central element with this average.*

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


#Method 2- Gaussian Filtering

#Should specify the width and height of the kernel which should be positive and odd.
#We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively

blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


#Method 3- Median Filtering
#computes the median of all the pixels under the kernel window and the central pixel is replaced with this median value. 
#This is highly effective in removing salt-and-pepper noise. 

median = cv2.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()



#Method 4- Bilateral Filtering
# highly effective at noise removal while preserving edges. 
# But the operation is slower compared to other filters.

blur = cv2.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()













