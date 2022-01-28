from cv2 import *
import cv2

# # initialize the camera
# cam = VideoCapture(0)   # 0 -> index of camera
# s, img = cam.read()
# if s:    # frame captured without any errors
    
    # imshow("cam-test",img)
    # waitKey(0)
    # destroyWindow("cam-test")
    # imwrite("filename.jpg",img) #save image
    
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img1 = cam.read()
ret = cam.set(3,1920);      #width
ret = cam.set(4,1080);      #height
# # ret = cam.set(10,20);      #brightness
# # ret = cam.set(11,50 );      #contrast
# # ret = cam.set(12,80);     #Saturation
# # ret = cam.set(15,40);     #Exposure

if s:    # frame captured without any errors
    #cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow("cam-test",img1)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("Scene.jpg",img1) #save image
del(cam)