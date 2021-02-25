import cv2
import numpy as np
img1 = cv2.imread("miniproj/balloons.jpg")
img2 = img1.copy()
#extract red color
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,np.array([0,50,50]),np.array([13,255,255]))
red = cv2.bitwise_and(img2,img2,mask=mask)
#gray
gray = cv2.cvtColor(red,cv2.COLOR_BGR2GRAY)
#noise removal and Dilate
opening = cv2.morphologyEx(
        gray,
        cv2.MORPH_CLOSE,
        np.ones((3,3),
        np.uint8),
        iterations=1)
opening = cv2.morphologyEx(
        opening,
        cv2.MORPH_OPEN,
        np.ones((3,3),
        np.uint8),
        iterations=1)

#Threshold
_,thres = cv2.threshold(opening,55,255,cv2.THRESH_BINARY)

#Distance
dist = cv2.distanceTransform(thres,cv2.DIST_L1,3)

#normalize
cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
distu = np.uint8(dist)

#Threshold & Marker
_,thr_dist = cv2.threshold(distu,0.5*dist.max(),255,cv2.THRESH_BINARY)
mark_obj = cv2.subtract(thres,thr_dist)

#Marker label
_,marker_label = cv2.connectedComponents(thr_dist)

#show number of obj
min_value,max_value,p1,p2 = cv2.minMaxLoc(marker_label)

#Add one to all label
marker_label=marker_label+1

marker_label[mark_obj==255]=0
#show all obj
marker_show = (marker_label*20).astype('uint8')
#watershed transform
marker_label = cv2.watershed(img1,marker_label)

img1[marker_label==-1]=[0,255,0]

cv2.imshow("Original",img1)
cv2.imshow("Gray",mask)
# cv2.imshow("Distance",distu)
# cv2.imshow("Marker Object",mark_obj)
# cv2.imshow("Marker Label",marker_show)
cv2.waitKey(0)
cv2.destroyAllWindows()