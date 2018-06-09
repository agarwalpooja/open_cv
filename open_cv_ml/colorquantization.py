import numpy as np
import cv2 as cv
img = cv.imread('1.jpeg')
Z = img.reshape((-1,3))
print(Z)
cv.imshow('input',img)
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
print(center)
# Now convert back into uint8, and make original image
center = np.uint8(center)
print(center)
res = center[label.flatten()]
print(res)
res2 = res.reshape((img.shape))
print(res2)
cv.imshow('res2',res2)
cv.waitKey(0)
cv.destroyAllWindows()