import cv2
import numpy as np

img = cv2.imread("dataset/coins.jpg")
print(img.shape)

rows,cols,ch = img.shape

#Rotation
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) #rotate 90 degree
res = cv2.warpAffine(img,M,(cols,rows))

print(M)

cv2.imshow("original",img)
cv2.imshow("result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()