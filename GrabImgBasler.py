#!/usr/bin/python
import datetime
from pypylon import pylon
from pypylon import genicam
import cv2
import sys
import os

# Number of images to be grabbed.
countOfImagesToGrab = 1
now = datetime.datetime.now()
now = datetime.datetime.now()
time = now.strftime("%d%m%Y")
print(time)
path= "D:/AlgoCharbel/images"
print(path)
dirName=path+"/"+time


# The exit code of the sample application.
exitCode = 0

try:
    # Create an instant camera object with the camera device found first.
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

    # Print the model name of the camera.
    print("Using device ", camera.GetDeviceInfo().GetModelName())

    # The parameter MaxNumBuffer can be used to control the count of buffers
    # allocated for grabbing. The default value of this parameter is 10.
    camera.MaxNumBuffer = 5

    # Start the grabbing of c_countOfImagesToGrab images.
    # The camera device is parameterized with a default configuration which
    # sets up free-running continuous acquisition.
    camera.StartGrabbingMax(countOfImagesToGrab)
    converter = pylon.ImageFormatConverter()

    # converting to opencv bgr format
    converter.OutputPixelFormat = pylon.PixelType_BGR8packed
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    # Camera.StopGrabbing() is called automatically by the RetrieveResult() method
    # when c_countOfImagesToGrab images have been retrieved.
    while camera.IsGrabbing():
        # Wait for an image and then retrieve it. A timeout of 5000 ms is used.
        grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Image grabbed successfully?
        if grabResult.GrabSucceeded():
            # Access the image data.
            print("SizeX: ", grabResult.Width)
            print("SizeY: ", grabResult.Height)
            img = grabResult.Array
            print("Gray value of first pixel: ", img[0, 0])
            image = converter.Convert(grabResult)
            img = image.GetArray()
            cv2.imshow("main",cv2.resize(img, (800,600)))
            name = now.strftime("%d%m%Y-%H%M%S")+'.jpg'
            if os.path.isdir(path+"/"+time) == True:
                print("path exists")
                cv2.imwrite(dirName+"/"+name,img)
            else :
                print("path doesnt exists")
                os.mkdir(dirName)
                print("Directory " , dirName ,  " Created ")
                cv2.imwrite(dirName+"/"+name,img)
            
            pythonscript  = "D:/AlgoCharbel/Algorithmedeeplearning/keras files/predict_resnet50-Copy.py"           
            exec(open(pythonscript).read())
        else:
            print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
        grabResult.Release()
except genicam.GenericException as e:
    # Error handling.
    print("An exception occurred.")
    print(e.GetDescription())
    exitCode = 1
sys.exit(exitCode)

