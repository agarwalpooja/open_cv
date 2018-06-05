# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:57:37 2018

@author: ASUS
"""

import numpy as np
import cv2 as cv
img=cv.imread('2.jpeg',1)
cv.imshow('image',img)
k = cv.waitKey(0) &0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord(s):
    cv.imwrite("play.jpeg",img)        
    cv.destroyAllWindows()

    