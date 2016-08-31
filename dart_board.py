import sys
import numpy as np
import cv2
from itertools import cycle

try:

    # draw circle at the center of the canvas

    circle_canvas = np.zeros( (330, 330, 3), dtype="uint8" )
    (centerX, centerY) = (circle_canvas.shape[1]/2, circle_canvas.shape[0]/2)
    red = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)

    colors = [black, white]
    color_picker = cycle(range(len(colors)))
    for r in xrange(0, 175, 25):
        if r == 0:
            cv2.circle(circle_canvas, (centerX, centerY), r, red, 20 )
        else:            
            color = colors[color_picker.next()]
            cv2.circle(circle_canvas, (centerX, centerY), r, color, 15 )
        # cv2.circle(circle_canvas, (centerX, centerY), r, white )

    # draw concentric circles

    cv2.imshow("Canvas", circle_canvas)
    while(1):
        cv2.waitKey(33)

except KeyboardInterrupt:
    # save the image -- OpenCV handles converting filetypes
    # automatically
    print "Exiting."
    sys.exit(0)