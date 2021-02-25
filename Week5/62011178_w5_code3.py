import cv2
import numpy as np
img1 = cv2.imread("dataset/colorobject.png")
img2 = img1.copy()
#extract red color
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,np.array([0,50,50]),np.array([10,255,255]))
res = cv2.bitwise_and(img2,img2,mask=mask)
#Threshold
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
_,thr = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

#Drawing Contours
contours,_ = cv2.findContours(thr,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(img2,contours,i,(255,255,255),3)

cv2.imshow("Original",img1)
cv2.imshow("Result",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()