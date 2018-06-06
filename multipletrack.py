# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:40:26 2018

@author: ASUS
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255]) 
    green_mask = cv2.inRange(hsv, lower_green, upper_green) # I have the Green threshold image.
    
    lower_red = np.array([-10, 100, 100])
    upper_red = np.array([10, 255, 255]) 
    red_mask = cv2.inRange(hsv, lower_red, upper_red) # I have the Green threshold image.


    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = blue_mask + green_mask+red_mask

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    plt.imshow(frame)
    plt.show()
    plt.imshow(mask)
    plt.show()
    plt.imshow(res)
    plt.show()
    
