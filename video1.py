# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:04:43 2018

@author: ASUS
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
cap=cv.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    if ret is True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
        ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
        print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    else:
        break
    plt.imshow(gray)
    plt.show()
cap.release()