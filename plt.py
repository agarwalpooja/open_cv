# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:01:06 2018

@author: ASUS
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('2.jpeg',-1)
b,g,r=cv.split(img)
img2=cv.merge([r,g,b])
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()