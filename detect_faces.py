# import the necessary packages
import cv2

# load our image and convert it to grayscale
image = cv2.imread("images/orientation_example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
detector = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7,
    minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)

# loop over the faces and draw a rectangle surrounding each
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the detected faces
try:
    while(1):
        cv2.imshow("Faces", image)
        wait = cv2.waitKey(33)
except KeyboardInterrupt:
    # wait key values are platform dependent.
    print
    print "Exiting."
