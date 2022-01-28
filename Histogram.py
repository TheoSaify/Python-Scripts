import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt


img = cv2.imread('img1.png',0)

# color = ('b','g','r')
# for i,col in enumerate(color):
    # histr = cv2.calcHist([img],[i],None,[256],[0,256])
    # plt.plot(histr,color = col)
    # plt.xlim([0,256])
# plt.show()


hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()