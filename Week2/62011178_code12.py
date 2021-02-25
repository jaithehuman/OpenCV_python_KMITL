import cv2
import numpy as np

img = cv2.imread("dataset/sudoku.jpg",0)
print(img.shape)

rows,cols = img.shape

#Perspective : 4 input points
#point1 p1(56,65)   p2(368,52)  p3(28,387)  p4(389,390)
#point2 p1(0,0)     p2(300,0)   p3(0,300)   p4(300,300)
w=420
h=420

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])

M = cv2.getPerspectiveTransform(pts1,pts2)
print(M) #matrix 3x3

res = cv2.warpPerspective(img,M,(w,h)) #300,300 mean new img size [width,height]

cv2.imshow("original",img)
cv2.imshow("result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()