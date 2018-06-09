import numpy as np
import cv2 
import matplotlib.pyplot as plt

img1=cv2.imread('img1.png')
img2=cv2.imread('img2.png')
img3=cv2.imread('closing.png')
img4=cv2.imread('img4.jpg')
#img5=cv2.imread('dialation.png')
img6=cv2.imread('j.png')
img7=cv2.imread('opening.png')

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

img_dilation1 = cv2.dilate(img1, kernel, iterations=1)
img_dilation2= cv2.dilate(img2, kernel, iterations=1)
img_dilation3 = cv2.dilate(img3, kernel, iterations=1)
img_dilation4 = cv2.dilate(img4, kernel, iterations=1)
#img_dilation5 = cv2.dilate(img5, kernel, iterations=1)
img_dilation6 = cv2.dilate(img6, kernel, iterations=1)
img_dilation7 = cv2.dilate(img7, kernel, iterations=1)

img_dilation31 = cv2.dilate(img3, kernel1, iterations=1)


cv2.imshow('Input', img1)
cv2.imshow('Dilation', img_dilation1)
cv2.waitKey(0)

cv2.imshow('Input', img2)
cv2.imshow('Dilation', img_dilation2)
cv2.waitKey(0)

cv2.imshow('Input', img3)
cv2.imshow('Dilation', img_dilation3)
cv2.imshow('Dilation1', img_dilation31)
cv2.waitKey(0)

cv2.imshow('Input', img4)
cv2.imshow('Dilation', img_dilation4)
cv2.waitKey(0)

#cv2.imshow('Input', img5)
#cv2.imshow('Dilation', img_dilation5)
cv2.imshow('Input', img6)
cv2.imshow('Dilation', img_dilation6)
cv2.waitKey(0)

cv2.imshow('Input', img7)
cv2.imshow('Dilation', img_dilation7)

cv2.waitKey(0)
cv2.destroyAllWindows()