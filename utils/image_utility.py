import os
import sys
import numpy as np
import cv2

def translate(image, x, y):
    ''' given image np translates / shifts / moves the image w.r.t (x, y) coordinate. '''
    # define the translation matrix and perform the translation
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
 
    # return the translated image
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    ''' given image np rotates the image to angle, w.r.t (x, y) coordinate. '''
    # grab the dimensions of the image
    (h, w) = image.shape[:2]

    # if the center is None, initialize it as the center of
    # the image
    if center is None:
        center = (w / 2, h / 2)

    # perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    # return the rotated image
    return rotated

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    ''' given image np resizes the image to new width or height. 
        Note: optional inter values.
              1. cv2.INTER_NEAREST
              2. cv2.INTER_LINEAR (downsizing)
              3. cv2.INTER_AREA (popular)
              4. cv2.INTER_CUBIC (upsizing)
              5. cv2.INTER_LANCZOS4

    '''
    
    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]
 
    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
 
    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))
 
    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)
 
    # return the resized image
    return resized
