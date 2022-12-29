import cv2
import numpy as np
from matplotlib import pyplot as plt

def readGreyScale(imgPath):
    grayA = cv2.imread('lena.jpg',0)
    return grayA
