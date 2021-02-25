from cv2 import cv2
img = cv2.imread("dataset/flower.jpg",1)

cv2.imshow("RGB color",img)

#Convert RGB to Gray

gy = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("Gray color",gy)
cv2.waitKey(0)
cv2.destroyAllWindows()