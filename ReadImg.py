import numpy as np
import cv2
from matplotlib import pyplot as plt

#load an color image in grayscale
img = cv2.imread('C://Users//alsaifyt//Desktop//PythonOpenCvScripts//imgColorC.png',0)



#Display image in a Window
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created

#Save an image
#cv2.imwrite('messigray.png',img)