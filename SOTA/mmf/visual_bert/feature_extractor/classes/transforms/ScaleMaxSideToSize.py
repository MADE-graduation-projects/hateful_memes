import cv2
import numpy as np


class ScaleMaxSideToSize(object):
    def __init__(self, size):
        self.size = size

    def __call__(self, sample):
        sample = cv2.resize(sample, (self.size, self.size), interpolation=cv2.INTER_AREA)
       
        return sample