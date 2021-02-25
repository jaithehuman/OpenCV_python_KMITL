import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv,np.array([155,25,0]),np.array([179,255,255]))
res_hsv = cv2.bitwise_and(img,img,mask=mask)

grayImage = cv2.cvtColor(res_hsv, cv2.COLOR_BGR2GRAY)
  
#min = 50 max = 255
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 50, 255, cv2.THRESH_BINARY)

canny = cv2.Canny(blackAndWhiteImage,threshold1=0,threshold2=50)

cv2.imshow("image",img)
cv2.imshow("HSV",res_hsv)
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()