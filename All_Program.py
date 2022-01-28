import cv2
from cv2 import *
import numpy as np
from matplotlib import pyplot as plt




###############################SIFT MATCH Function#################################
def SIFTMATCH(img1,img2):

    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)


    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
        print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
        matchesMask = None
        
        
    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                       singlePointColor = None,
                       matchesMask = matchesMask, # draw only inliers
                       flags = 2)

    img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)


    cv2.moveWindow('output', 150,150)  # Move it to (40,30)
    cv2.imshow('output',img3)
    cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
    cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created

###################################################################################################

#################################Function#########################

def CercleDetection(img1):
    # Read Image
    raw_image = cv2.imread(img1)

    # Bilateral filtering forms a very good way to preserve edges. It is a non-linear filter and helps reduce noise 
    # The parameters used are: the image, window size for averaging the neighbour, sigmaColor(Sigma value in the color space. 
    bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)

    # Canny edge detector to detect edges in the image It takes 3 parameters: image, lower threshold and upper threshold.
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)


    # Find Contours
    _, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 50000) ):
            contour_list.append(contour)
            print("area %.3f"%(area))
            M = cv2.moments(contour)
            # calculate x,y coordinate of center
            if M["m00"] != 0:
             cX = int(M["m10"] / M["m00"])
             cY = int(M["m01"] / M["m00"])
            else:
             cX, cY = 0, 0
            cv2.circle(raw_image, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(raw_image, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


            
            
    # Draw Contours of circles
    cv2.drawContours(raw_image, contour_list, -1, (0, 255, 0), 3)
   
    # Display Images
    cv2.imshow("Objects Detected",raw_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return cX,cY

############################################################
    
###########################MAIN#############################   
    
MIN_MATCH_COUNT = 10
e1 = cv2.getTickCount()


# # initialize the camera
# cam = VideoCapture(0)   # 0 -> index of camera
# s, img1 = cam.read()
# ret = cam.set(3,1920);
# ret = cam.set(4,1080);

# if s:    # frame captured without any errors
    # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    # cv2.imshow("cam-test",img1)
    # waitKey(0)
    # destroyWindow("cam-test")
    # imwrite("Scene.jpg",img1) #save image
# del(cam)



# Scene image in Grayscale
# imgray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
imgray = cv2.imread('Scene.jpg', 0) # queryImage


# Reference Piece Image
img1 = cv2.imread('img3.jpg',0) # queryImage
    
# SIFT Algorithm fore Object Detection
SIFTMATCH(img1, imgray)


# image de reference
cX, cY = CercleDetection('img3.jpg')
print('cX = %.3f , cY =%.3f' % (cX, cY))



# Image Webcam

cX2, cY2 = CercleDetection('img3.jpg')
print('cX2 = %.3f , cY2 =%.3f' % (cX2, cY2))


deltaX = (cX2-cX)
deltaY = -(CY2-cY)


# Write X and Y values to File
file = open("values.txt", "w")
file.write("%.3f \n" % deltaX)
file.write("%.3f \n" % deltaY)
file.close() 






#Calculate time of execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print('time needed to execute')
print(time)





