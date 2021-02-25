from cv2 import cv2
#print(cv2.__version__)

img = cv2.imread("dataset/flower.jpg")
cv2.imshow("My Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()