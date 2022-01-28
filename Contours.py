import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt


#Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity.
#The contours are a useful tool for shape analysis and object detection and recognition

im = cv2.imread('img1.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# To draw all the contours in an image:
image = cv2.drawContours(image, contours, -1, (255,255,0), 3)

# To draw an individual contour, say 4th contour
# img = cv2.drawContours(img, contours, 3, (0,255,0), 3)

# OR

# cnt = contours[4]
# img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)


print(len(contours))

cnt = contours[10]
M = cv2.moments(cnt)


print(f'Contours 0 Moments ={M}')
area = cv2.contourArea(cnt)

print(f'area = {area}')


perimeter = cv2.arcLength(cnt,True)
print(f'perimeter = {perimeter}')

x,y,w,h = cv2.boundingRect(cnt)
image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
image = cv2.drawContours(image,[box],0,(0,0,255),2)


	
cv2.imshow('image',image)
cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created