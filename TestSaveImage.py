import datetime
from pypylon import pylon
from pypylon import genicam
import cv2
import sys
import os



now = datetime.datetime.now()
time = now.strftime("%d%m%Y")
print(time)
name = now.strftime("%d%m%Y-%H%M%S")+'.jpg'
path= "D:/AlgoCharbel/images"
print(path)
dirName=path+"/"+time
print(dirName)


if os.path.isdir(path+"/"+time) == True:
	print("path exists")
	print(name)

else :
	print("path doesnt exists")
	os.mkdir(dirName)
	print("Directory " , dirName ,  " Created ")
	print(name)
