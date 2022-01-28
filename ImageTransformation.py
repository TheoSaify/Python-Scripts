import cv2
import numpy as np


###############################SCALING#########################

img = cv2.imread('C://Users//alsaifyt//Desktop//PythonOpenCvScripts//dave.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)      #interpolation cv2.INTER_AREA for shrinking 
																			#cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)



###############################Translation#########################

rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))      #Third argument of the cv2.warpAffine() function is the size of the output image (width,height)

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()




###############################Rotation#########################

rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)  #rotates the image by 90 degree with respect to center without any scaling
dst = cv2.warpAffine(img,M,(cols,rows))




###############################Affine Transformation#########################
								# all parallel lines in the original image will still be parallel in the output image #

rows,cols,ch = img.shape	

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()


###############################Perspective Transformation#########################


rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()







