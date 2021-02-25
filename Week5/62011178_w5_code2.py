import cv2
import numpy as np

img = cv2.imread("dataset/watershed.jpg")

#gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#noise removal and Dilate
opening = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,np.ones((4,4),np.uint8),iterations=1)
opening = cv2.morphologyEx(opening,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=1)
#Threshold
_,thres = cv2.threshold(opening,226,255,cv2.THRESH_BINARY_INV)
#Distance
dist = cv2.distanceTransform(thres,cv2.DIST_L2,3)
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
marker_label = cv2.watershed(img,marker_label)
# #show result
# for x in range(2,15):
#     img[marker_label==x]=[np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256)]
img[marker_label==-1]=[0,0,255]
cv2.imshow("Original",img)
cv2.imshow("Gray",gray)
cv2.imshow("Distance",distu)
cv2.imshow("Marker Object",mark_obj)
cv2.imshow("Marker Label",marker_show)
cv2.waitKey(0)
cv2.destroyAllWindows()