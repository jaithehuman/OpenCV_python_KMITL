#Thresholding techniques

from cv2 import cv2
from matplotlib import pyplot as plot

img = cv2.imread("dataset/graylevel.jpg",0)

ret,thres = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)

cv2.imshow("Gray level",img)
cv2.imshow("Threshold image",thres)
cv2.waitKey(0)
cv2.destroyAllWindows()