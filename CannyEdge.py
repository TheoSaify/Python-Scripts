import cv2
import numpy as np
from matplotlib import pyplot as plt



# Stage 1 - Noise Reduction with 5*5 Gaussian Filter
# Stage 2 - Finding Intensity Gradient of the Image
# (Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction (G_x) and vertical direction (G_y))
# Stage 3 - Non-maximum Suppression (every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient)
# Stage 4 - Hysteresis Thresholding



img = cv2.imread('dave.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()