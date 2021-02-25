#How to know the dimension of image
from cv2 import cv2

img = cv2.imread("dataset/flower.jpg",0)
print(img.shape)

cv2.imshow("Gray Color",img)

cv2.waitKey(0)
cv2.destroyAllWindows()