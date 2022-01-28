import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('dave.jpg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
cv2.drawKeypoints(img, kp, None,color=(255,0,0))



cv2.imwrite('fast_true.png',img)

# Disable nonmaxSuppression

kp = fast.detect(img,None)

print ("Total Keypoints without nonmaxSuppression: ", len(kp))

cv2.drawKeypoints(img, kp, None)

cv2.imwrite('fast_false.png',img)

cv2.imshow('image',img)
cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created