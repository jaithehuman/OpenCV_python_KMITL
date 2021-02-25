import cv2
import numpy as np

img = cv2.imread("dataset/coins2.jpg",0)
_,thr = cv2.threshold(img,80,255,cv2.THRESH_BINARY)

closing = cv2.morphologyEx(thr,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8),iterations=2)
dist = cv2.distanceTransform(closing,cv2.DIST_L2,3)

cv2.normalize(dist,dist,0,1.0,cv2.NORM_MINMAX)

cv2.imshow("image",img)
cv2.imshow("Distance",dist)
cv2.waitKey(0)
cv2.destroyAllWindows()