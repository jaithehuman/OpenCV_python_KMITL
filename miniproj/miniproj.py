import cv2
import numpy as np
img1 = cv2.imread("miniproj/redcar.jpg")

#resize
img_resize = cv2.resize(img1,None,fx=0.2,fy=0.2)
img2 = img_resize.copy()

#extract red color
hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,np.array([0,50,50]),np.array([10,255,255]))
red = cv2.bitwise_and(img_resize,img_resize,mask=mask)
#gray
gray = cv2.cvtColor(red,cv2.COLOR_BGR2GRAY)

#Threshold
_,thres = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

#Opening

opening = cv2.morphologyEx(
        thres,
        cv2.MORPH_OPEN,
        np.ones((3,3),
        np.uint8),
        iterations=2)
#Closing
closing = cv2.morphologyEx(
        opening,
        cv2.MORPH_CLOSE,
        np.ones((3,3),
        np.uint8),
        iterations=10)
#Dilating
dilating = cv2.morphologyEx(
        closing,
        cv2.MORPH_DILATE,
        np.ones((3,3),
        np.uint8),
        iterations=4)


#Distance
dist = cv2.distanceTransform(dilating,cv2.DIST_L2,3)

#normalize
cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
distu = np.uint8(dist)

#Threshold & Marker
_,thr_dist = cv2.threshold(distu,0.02*dist.max(),255,cv2.THRESH_BINARY)
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
marker_label = cv2.watershed(img_resize,marker_label)

img2[marker_label==2]=[0,255,255]


cv2.imshow("Original",img_resize)
cv2.imshow("HSV",hsv)
cv2.imshow("Gray",mask)
cv2.imshow("Closing",closing)
cv2.imshow("Opening",opening)
cv2.imshow("Dilating",dilating)
cv2.imshow("Threshold",thres)
cv2.imshow("Distance",distu)
cv2.imshow("Result",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Second Picture
# img1 = cv2.imread("miniproj/bluedress.jpg")

# #resize
# img_resize = cv2.resize(img1,None,fx=0.6,fy=0.6)
# img2 = img_resize.copy()

# #extract blue color
# hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv,np.array([100,50,50]),np.array([140,255,255]))
# red = cv2.bitwise_and(img_resize,img_resize,mask=mask)
# #gray
# gray = cv2.cvtColor(red,cv2.COLOR_BGR2GRAY)

# #Threshold
# _,thres = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

# #Opening

# opening = cv2.morphologyEx(
#         thres,
#         cv2.MORPH_OPEN,
#         np.ones((3,3),
#         np.uint8),
#         iterations=0)
# #Closing
# closing = cv2.morphologyEx(
#         opening,
#         cv2.MORPH_CLOSE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=1)
# #Dilating
# dilating = cv2.morphologyEx(
#         closing,
#         cv2.MORPH_DILATE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=1)


# #Distance
# dist = cv2.distanceTransform(dilating,cv2.DIST_L2,3)

# #normalize
# cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
# distu = np.uint8(dist)

# #Threshold & Marker
# _,thr_dist = cv2.threshold(distu,0.01*dist.max(),255,cv2.THRESH_BINARY)
# mark_obj = cv2.subtract(thres,thr_dist)

# #Marker label
# _,marker_label = cv2.connectedComponents(thr_dist)

# #show number of obj
# min_value,max_value,p1,p2 = cv2.minMaxLoc(marker_label)

# #Add one to all label
# marker_label=marker_label+1

# marker_label[mark_obj==255]=0
# #show all obj
# marker_show = (marker_label*20).astype('uint8')
# #watershed transform
# marker_label = cv2.watershed(img_resize,marker_label)

# img2[marker_label==2]=[0,0,255]


# cv2.imshow("Original",img_resize)
# cv2.imshow("HSV",hsv)
# cv2.imshow("Gray",mask)
# cv2.imshow("Closing",closing)
# cv2.imshow("Opening",opening)
# cv2.imshow("Dilating",dilating)
# cv2.imshow("Threshold",thres)
# cv2.imshow("Distance",distu)
# # cv2.imshow("Marker Object",mark_obj)
# # cv2.imshow("Marker Label",marker_show)
# cv2.imshow("Result",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Third Picture
# img1 = cv2.imread("miniproj/greentea.jpg")

# #resize
# img_resize = cv2.resize(img1,None,fx=0.6,fy=0.6)
# img2 = img_resize.copy()

# #extract green color
# hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv,np.array([20,50,50]),np.array([50,255,255]))
# red = cv2.bitwise_and(img_resize,img_resize,mask=mask)
# #gray
# gray = cv2.cvtColor(red,cv2.COLOR_BGR2GRAY)

# #Threshold
# _,thres = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

# #Opening

# opening = cv2.morphologyEx(
#         thres,
#         cv2.MORPH_OPEN,
#         np.ones((3,3),
#         np.uint8),
#         iterations=0)
# #Closing
# closing = cv2.morphologyEx(
#         opening,
#         cv2.MORPH_CLOSE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=0)
# #Dilating
# dilating = cv2.morphologyEx(
#         closing,
#         cv2.MORPH_DILATE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=0)


# #Distance
# dist = cv2.distanceTransform(dilating,cv2.DIST_L2,3)

# #normalize
# cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
# distu = np.uint8(dist)

# #Threshold & Marker
# _,thr_dist = cv2.threshold(distu,0.01*dist.max(),255,cv2.THRESH_BINARY)
# mark_obj = cv2.subtract(thres,thr_dist)

# #Marker label
# _,marker_label = cv2.connectedComponents(thr_dist)

# #show number of obj
# min_value,max_value,p1,p2 = cv2.minMaxLoc(marker_label)

# #Add one to all label
# marker_label=marker_label+1

# marker_label[mark_obj==255]=0
# #show all obj
# marker_show = (marker_label*20).astype('uint8')
# #watershed transform
# marker_label = cv2.watershed(img_resize,marker_label)

# img2[marker_label==2]=[0,160,255]


# cv2.imshow("Original",img_resize)
# cv2.imshow("HSV",hsv)
# cv2.imshow("Gray",mask)
# cv2.imshow("Closing",closing)
# cv2.imshow("Opening",opening)
# cv2.imshow("Dilating",dilating)
# cv2.imshow("Threshold",thres)
# cv2.imshow("Distance",distu)
# # cv2.imshow("Marker Object",mark_obj)
# # cv2.imshow("Marker Label",marker_show)
# cv2.imshow("Result",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Fourth Picture
# img1 = cv2.imread("miniproj/banana.jpg")

# #resize
# img_resize = cv2.resize(img1,None,fx=0.1,fy=0.1)
# img2 = img_resize.copy()

# #extract green color
# hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv,np.array([20,50,50]),np.array([50,255,255]))
# red = cv2.bitwise_and(img_resize,img_resize,mask=mask)
# #gray
# gray = cv2.cvtColor(red,cv2.COLOR_BGR2GRAY)

# #Threshold
# _,thres = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

# #Opening

# opening = cv2.morphologyEx(
#         thres,
#         cv2.MORPH_OPEN,
#         np.ones((3,3),
#         np.uint8),
#         iterations=1)
# #Closing
# closing = cv2.morphologyEx(
#         opening,
#         cv2.MORPH_CLOSE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=1)
# #Dilating
# dilating = cv2.morphologyEx(
#         closing,
#         cv2.MORPH_DILATE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=1)


# #Distance
# dist = cv2.distanceTransform(dilating,cv2.DIST_L2,3)

# #normalize
# cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
# distu = np.uint8(dist)

# #Threshold & Marker
# _,thr_dist = cv2.threshold(distu,0.01*dist.max(),255,cv2.THRESH_BINARY)
# mark_obj = cv2.subtract(thres,thr_dist)

# #Marker label
# _,marker_label = cv2.connectedComponents(thr_dist)

# #show number of obj
# min_value,max_value,p1,p2 = cv2.minMaxLoc(marker_label)

# #Add one to all label
# marker_label=marker_label+1

# marker_label[mark_obj==255]=0
# #show all obj
# marker_show = (marker_label*20).astype('uint8')
# #watershed transform
# marker_label = cv2.watershed(img_resize,marker_label)

# img2[marker_label==2]=[70,230,100]


# cv2.imshow("Original",img_resize)
# cv2.imshow("HSV",hsv)
# cv2.imshow("Gray",mask)
# cv2.imshow("Closing",closing)
# cv2.imshow("Opening",opening)
# cv2.imshow("Dilating",dilating)
# cv2.imshow("Threshold",thres)
# cv2.imshow("Distance",distu)
# # cv2.imshow("Marker Object",mark_obj)
# # cv2.imshow("Marker Label",marker_show)
# cv2.imshow("Result",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #Fifth Picture
# img1 = cv2.imread("miniproj/strawberry.jpg")

# #resize
# img_resize = cv2.resize(img1,None,fx=0.3,fy=0.3)
# img2 = img_resize.copy()

# #extract green color
# hsv = cv2.cvtColor(img_resize,cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv,np.array([0,50,50]),np.array([20,255,255]))
# red = cv2.bitwise_and(img_resize,img_resize,mask=mask)
# #gray
# gray = cv2.cvtColor(red,cv2.COLOR_BGR2GRAY)

# #Threshold
# _,thres = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

# #Opening

# opening = cv2.morphologyEx(
#         thres,
#         cv2.MORPH_OPEN,
#         np.ones((3,3),
#         np.uint8),
#         iterations=0)
# #Closing
# closing = cv2.morphologyEx(
#         opening,
#         cv2.MORPH_CLOSE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=3)
# #Dilating
# dilating = cv2.morphologyEx(
#         closing,
#         cv2.MORPH_DILATE,
#         np.ones((3,3),
#         np.uint8),
#         iterations=0)


# #Distance
# dist = cv2.distanceTransform(dilating,cv2.DIST_L2,3)

# #normalize
# cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
# distu = np.uint8(dist)

# #Threshold & Marker
# _,thr_dist = cv2.threshold(distu,0.01*dist.max(),255,cv2.THRESH_BINARY)
# mark_obj = cv2.subtract(thres,thr_dist)

# #Marker label
# _,marker_label = cv2.connectedComponents(thr_dist)

# #show number of obj
# min_value,max_value,p1,p2 = cv2.minMaxLoc(marker_label)

# #Add one to all label
# marker_label=marker_label+1

# marker_label[mark_obj==255]=0
# #show all obj
# marker_show = (marker_label*20).astype('uint8')
# #watershed transform
# marker_label = cv2.watershed(img_resize,marker_label)

# for x in range(2,15):
#      img2[marker_label==x]=[np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256)]

# cv2.imshow("Original",img_resize)
# cv2.imshow("HSV",hsv)
# cv2.imshow("Gray",mask)
# cv2.imshow("Closing",closing)
# cv2.imshow("Opening",opening)
# cv2.imshow("Dilating",dilating)
# cv2.imshow("Threshold",thres)
# cv2.imshow("Distance",distu)
# # # cv2.imshow("Marker Object",mark_obj)
# # # cv2.imshow("Marker Label",marker_show)
# cv2.imshow("Result",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()