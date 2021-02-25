from cv2 import cv2
from matplotlib import pyplot as plot
import numpy as np
img = cv2.imread("dataset/graylevel.jpg",0)

ret,thres1 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO)

ret,thres2 = cv2.threshold(thres1,210,255,cv2.THRESH_TOZERO_INV)

ret,thres3 = cv2.threshold(thres2,100,255,cv2.THRESH_BINARY)

resGx = cv2.Sobel(thres3,cv2.CV_64F,1,0)
resGy = cv2.Sobel(thres3,cv2.CV_64F,0,1)
sobel = np.absolute(resGx) + np.absolute(resGy)

cv2.imshow("Original",img)
cv2.imshow("THRES_TOZERO",thres1)
cv2.imshow("THRES_TOZERO_INV",thres2)
cv2.imshow("THRES_BINARY",thres3)
cv2.imshow("Sobel",sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()