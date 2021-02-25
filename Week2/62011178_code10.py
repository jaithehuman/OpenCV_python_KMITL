import cv2
import numpy as np

img = cv2.imread("dataset/rectangle.png")
print(img.shape)

rows,cols,ch = img.shape

#point1     p1(257,72)  p2(594,230) p3(174,243)
#point2     p1(192,141) p2(566,141) p3(192,334) this is target position

pts1 = np.float32([[257,72],[594,230],[174,243]])
pts2 = np.float32([[192,141],[566,141],[192,334]])

M = cv2.getAffineTransform(pts1,pts2)
print(M)
res = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("original",img)
cv2.imshow("result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()