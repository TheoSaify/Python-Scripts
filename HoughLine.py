import cv2
import numpy as np


 # Hough Transform is a popular technique to detect any shape, if you can represent that shape in mathematical form
 
 img = cv2.imread('dave.jpg')
 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 edges = cv2.Canny(gray,50,150,apertureSize = 3)

 lines = cv2.HoughLines(edges,1,np.pi/180,200)
 for rho,theta in lines[0]:
     a = np.cos(theta)
     b = np.sin(theta)
     x0 = a*rho
	 y0 = b*rho
     x1 = int(x0 + 1000*(-b))
     y1 = int(y0 + 1000*(a))
     x2 = int(x0 - 1000*(-b))
     y2 = int(y0 - 1000*(a))

     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

 cv2.imwrite('houghlines3.jpg',img)

# img = cv2.imread('dave.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# minLineLength = 100
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
# for x1,y1,x2,y2 in lines[0]:
    # cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imwrite('houghlines5.jpg',img)

cv2.imshow('image',img)
cv2.waitKey(0)			  #The function waits for specified milliseconds for any keyboard event
cv2.destroyAllWindows()   #cv2.destroyAllWindows() simply destroys all the windows we created
