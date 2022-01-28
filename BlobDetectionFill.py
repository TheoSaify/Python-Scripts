import cv2;
import numpy as np;
 
# Read image
im_in = cv2.imread("scene.jpg", cv2.IMREAD_GRAYSCALE);
 
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
 
th, im_th = cv2.threshold(im_in, 170, 250, cv2.THRESH_BINARY_INV);
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
 
 # find contours in the binary image
im2, contours, hierarchy = cv2.findContours(im_floodfill_inv,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours_area = []
# calculate area and filter into new array
for con in contours:
    area = cv2.contourArea(con)
    if 45000 < area < 60000:
        contours_area.append(con)
        cv2.drawContours(im_floodfill_inv, contours, -1, (0, 255, 0), 3)

print(contours)
       
 
 
 
 
 
# Display images.
cv2.imshow(" Drawed contours", im2)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()