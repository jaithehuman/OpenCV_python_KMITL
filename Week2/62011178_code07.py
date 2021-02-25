from cv2 import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")
print(img.shape)

rows,cols,ch = img.shape

#Translation x = 100 pixel , y = 50 pixels
M = np.float32([[1,0,100],[0,1,50]])

res = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Original",img)
cv2.imshow("Result image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()