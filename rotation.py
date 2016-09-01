import os, sys
import numpy as np
import argparse
# import imutils
import cv2
 

sys.path.append(os.path.join(os.path.dirname(__file__),'utils'))
from utility import load_image

try:

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())
     
    # load the image and show it
    image = load_image(args["image"])
    cv2.imshow("Original", image)
     
    # grab the dimensions of the image and calculate the center of the image
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)
    # (cX, cY) = (50, 50)
     
    # rotate our image by 45 degrees
    M = cv2.getRotationMatrix2D((cX, cY), 110, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)
    print rotated[ 136, 312]
     
    # rotate our image by -90 degrees
    # M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
    # rotated = cv2.warpAffine(image, M, (w, h))
    # cv2.imshow("Rotated by -90 Degrees", rotated)
    while(1):
        cv2.waitKey(33)

except KeyboardInterrupt:
    print "Exiting."
    sys.exit(0)