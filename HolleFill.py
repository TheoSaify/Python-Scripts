import cv2;
import numpy as np;
 
# Read image
img = cv2.imread("scene.jpg");
gray = cv2.imread("scene.jpg",0);





# Display images.

cv2.imshow("gray image", gray)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()