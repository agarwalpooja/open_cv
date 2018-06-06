import numpy as np
import cv2 as cv
img = cv.imread('2.jpeg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
cv.imshow('res',res)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()