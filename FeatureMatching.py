import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('pieceTemplate.jpg',0)          # queryImage
img2 = cv2.imread('img21.jpg',0) # trainImage

def SIFTMATCH(img1,img2):
    img1=img1.copy()
    img2=img2.copy()
    sift = cv2.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)
    # Apply ratio test
    matchesMask = [[0,0] for i in range(len(matches))]
    for i,(m,n) in enumerate(matches):
        if 0.55*n.distance<m.distance < 0.80*n.distance:
            matchesMask[i]=[1,0]
            # cv2.drawMatchesKnn expects list of lists as matches.
    img3=None
    draw_params=dict(matchesMask=matchesMask)
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2,**draw_params)
#    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img3,flags=2)
    cv2.imshow('gray',img3)
    cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
    cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created
	
	
SIFTMATCH(img1,img2)