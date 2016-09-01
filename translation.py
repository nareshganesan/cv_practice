import os
import sys
import numpy as np
import argparse
# import imutils
import cv2

sys.path.append(os.path.join(os.path.dirname(__file__),'utils'))
from utility import load_image

try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image.")
    args = vars(ap.parse_args())

    image = load_image(args["image"])
    cv2.imshow("Original", image)

    # Translation code begins here

    M = np.float32([
            [1, 0, 25],
            [0, 1, 50]
        ])

    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]) )

    cv2.imshow("Shifted image", shifted)

    M = np.float32([
            [1, 0, -50],
            [0, 1, -90]
        ])
    top_shifted = cv2.warpAffine( image, M, (image.shape[1], image.shape[0]) )
    cv2.imshow("Shifted top left", top_shifted)

    while(1):
        cv2.waitKey(33)

except KeyboardInterrupt:
    print "Exiting."
    sys.exit(0)