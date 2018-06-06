# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:22:37 2018

@author: ASUS
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    plt.imshow(frame)
    plt.show()
    plt.imshow(mask)
    plt.show()
    plt.imshow(res)
    plt.show()
    