import cv2
import numpy as np

img = cv2.imread("dataset/coins.jpg")
kernel = np.ones((3,3),np.uint8)

_,bw = cv2.threshold(img,40,255,cv2.THRESH_BINARY)
opening = cv2.morphologyEx(bw,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(bw,cv2.MORPH_CLOSE,kernel,iterations=2)

cv2.imshow("Original",img)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()