import cv2
import numpy as np

img = cv2.imread("dataset/sudoku.jpg")


print(img.shape)


w=420
h=420

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])

M = cv2.getPerspectiveTransform(pts1,pts2)
print(M) #matrix 3x3

res = cv2.warpPerspective(img,M,(w,h)) 
res2 = cv2.warpPerspective(img,M,(w,h)) 

canny = cv2.Canny(res,threshold1=20,threshold2=60)

kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)


lines = cv2.HoughLinesP(closing,1,np.pi/360,190,minLineLength=50,maxLineGap=200)
print(len(lines))


for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(res2,(x1,y1),(x2,y2),(0,255,0),thickness = 3)


cv2.imshow("Original",img)
cv2.imshow("Perspective",res)
cv2.imshow("Canny Edge",canny)
cv2.imshow("Closing",closing)
cv2.imshow("Hough lines",res2)
cv2.waitKey(0)
cv2.destroyAllWindows()