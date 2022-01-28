import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img21.jpg',0)

# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
# surf = cv2.SURF(400)
surf = cv2.xfeatures2d.SURF_create()


# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img,None)
len(kp)

# Check present Hessian threshold
# print(surf.hessianThreshold)


# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
# surf.hessianThreshold = 50000

# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img,None)
print(len(kp))


img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)

plt.imshow(img2)
plt.show()



