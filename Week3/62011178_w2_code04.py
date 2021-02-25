import cv2
import numpy as np

img = cv2.imread("dataset/bikesgray.jpg")

kerGx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

kerGy = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

resGx = cv2.filter2D(img,0,kerGx)
resGy = cv2.filter2D(img,0,kerGy)

prewitt = np.absolute(resGx) + np.absolute(resGy)

resGx2 = cv2.Sobel(img,0,1,0,ksize=3)
resGy2 = cv2.Sobel(img,0,0,1,ksize=3)
sobel = np.absolute(resGx2) + np.absolute(resGy2)

canny = cv2.Canny(img,threshold1=180,threshold2=200)

cv2.imshow("Original",img)
cv2.imshow("Prewitt",prewitt)
cv2.imshow("Sobel",sobel)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

