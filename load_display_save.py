# import the necessary packages
import sys, argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-s", "--save", required=True, help="Path to save image")
args = vars(ap.parse_args())

print args["image"]

# load the image and show some basic information on it
image = cv2.imread(args["image"])
if not image.size:
    print "Image not found."
    sys.exit(0)
print "width: %d pixels" % (image.shape[1])
print "height: %d pixels" % (image.shape[0])
print "channels: %d" % (image.shape[2])

# show the image and wait for a keypress
try:
    while(1):
        cv2.imshow("Image", image)
        wait = cv2.waitKey(33)
except KeyboardInterrupt:
    # save the image -- OpenCV handles converting filetypes
    # automatically
    cv2.imwrite(args["save"], image)
    print "Image saved: %s" % args["save"]
    sys.exit(0)