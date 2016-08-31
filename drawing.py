import sys
import numpy as np
import cv2

try:

    canvas = np.zeros( (300, 300, 3), dtype="uint8" )

    # draw a green line from top left corner of our canvas
    # bottom right

    green = (0, 255, 0)
    cv2.line(canvas, (0, 0), (300, 300), green)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(33)


    # now, draw a 3 pixel thick red line from top-right corner
    # to bottom-left

    red = (0, 0, 255)
    cv2.line(canvas, (300, 0), (0, 300), red, 3)
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(33)

    # draw rectangle with different colors and thickness.

    cv2.rectangle(canvas, (10, 10), (50, 50), green )
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(33)

    cv2.rectangle(canvas, (50, 200), (200, 225), red, 5 )
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(33)

    blue = (255, 0, 0)
    cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1 )
    cv2.imshow("Canvas", canvas)
    # while(1):
    #     cv2.waitKey(33)

    # draw circle at the center of the canvas

    circle_canvas = np.zeros( (300, 300, 3), dtype="uint8" )
    (centerX, centerY) = (circle_canvas.shape[1]/2, canvas.shape[0]/2)
    white = (255, 255, 255)

    for r in xrange(0, 175, 25):
        cv2.circle(circle_canvas, (centerX, centerY), r, white )

    # draw concentric circles

    cv2.imshow("Canvas", circle_canvas)
    # while(1):
        # cv2.waitKey(33)

    for i in xrange(0, 25):
        radius = np.random.randint(5, high=20)
        color = np.random.randint(0, high=256, size=(3,)).tolist()
        pt = np.random.randint(0, high=300, size=(2,))

        print str(radius), str(color), str(pt)

        cv2.circle(circle_canvas, tuple(pt), radius, color, -1)
    cv2.imshow("Canvas", circle_canvas)
    # while(1):
    #     cv2.waitKey(33)

    image = cv2.imread("images/florida_trip.png")

    cv2.circle(image, (168, 188), 90, (0, 0, 255), 2 )
    cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
    cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
    cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

    cv2.imshow("Output", image)
    while(1):
        cv2.waitKey(33)

except KeyboardInterrupt:
    # save the image -- OpenCV handles converting filetypes
    # automatically
    print "Exiting."
    sys.exit(0)

