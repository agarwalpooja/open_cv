import numpy as np
import cv2 as cv
img = cv.imread('2.jpeg',0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.imshow('img1',img)
cv.waitKey(0)
cv.destroyAllWindows()