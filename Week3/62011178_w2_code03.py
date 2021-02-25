import cv2
import numpy as np

img = cv2.imread("dataset/butterfly.jpg")

ker = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

step1 = cv2.filter2D(img,0,ker)

res = cv2.Laplacian(step1,0,ksize=3)
cv2.imshow("Original",img)
cv2.imshow("Result image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()