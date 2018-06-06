import numpy as np
import cv2 as cv
img = cv.imread('2.jpeg',0)

height, width = img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(width,height))
cv.imshow('img',dst)
cv.imshow('img1',img)
cv.waitKey(0)
cv.destroyAllWindows()