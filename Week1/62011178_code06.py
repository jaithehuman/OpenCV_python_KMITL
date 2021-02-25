#HSV color mode / split object by using  color range

from cv2 import cv2
import numpy as np

img = cv2.imread("dataset/colorobject.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv,np.array([0,50,50]),np.array([10,255,255]))
res = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("image",img)
cv2.imshow("mask image",mask)
cv2.imshow("Result image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()