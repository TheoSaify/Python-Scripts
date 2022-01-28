import cv2
import numpy as np

img = cv2.imread('img21.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

kp= sift.detect(gray, None)
cv2.drawKeypoints(gray,kp,img)
cv2.imwrite('sift_keypoints.jpg',img)

cv2.imshow('image',img)
cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created



