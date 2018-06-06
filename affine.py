import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('2.jpeg')
rows,cols,ch = img.shape
print(rows)
print(cols)
pts1 = np.float32([[50,50],[20,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
print(M)
dst = cv.warpAffine(img,M,(cols,rows))
print(dst)
print(img)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()