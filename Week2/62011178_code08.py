import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")

rows,cols,ch = img.shape
#Scale X=0.5 , Y= 0.5
M = np.float32([[0.5,0,0],[0,0.5,0]])

res = cv2.warpAffine(img,M,(cols,rows),borderValue=(255,0,0)) #(blue,green,red)

cv2.imshow("Result image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()