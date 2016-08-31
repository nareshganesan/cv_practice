import os
import sys
import numpy as np
import cv2

import requests

from StringIO import StringIO
from PIL import Image

def load_image(image_path):
    ''' given an image path (local or http/s) returns the opencv image.'''
    try:
        if not image_exists(image_path):
            return None
        if ('https' in image_path) or ('http' in image_path):
            response = requests.get(image_path) 
            data = response.content
            pil_image = Image.open(StringIO(data)).convert('RGB')
            opencv_image = np.array(pil_image)
            # Convert RGB to BGR
            image = opencv_image[:, :, ::-1].copy() 
        else:
            image = cv2.imread(image_path)
        return image
    except Exception as e:
        print e
        return None



def image_exists(path):
    ''' given path (local or http/s) checks if the path is valid or exists. '''
    try:
        if not path:
            return False
        if ('https' in path) or ('http' in path):
            if path.endswith('.jpeg') or \
                path.endswith('.jpg') or \
                path.endswith('.png') or \
                path.endswith('.tiff') or \
                path.endswith('.tif'):

                resp = requests.head(path)
                if resp.status_code == 200:
                    return True
                else:
                    return False
            else:
                return False
        if not (os.path.exists(path) and os.path.isfile(path) ):
            return False
        return True
    except Exception as e:
        print e
        return False
