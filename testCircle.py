import cv2

e1 = cv2.getTickCount()
# Read Image
raw_image = cv2.imread('img3.jpg')

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


# Write X and Y values to File
file = open("values.txt","w") 
file.write("Centroid X and Y \n") 
file.write("%.3f \n"% (cX)) 
file.write("%.3f \n"% (cY)) 
file.close() 

#Calculate time of execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print('time needed to execute')
print(time)

# Display Images
cv2.imshow("Objects Detected",raw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()