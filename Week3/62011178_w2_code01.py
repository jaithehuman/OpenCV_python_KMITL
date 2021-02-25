import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")
np.set_printoptions(precision=3)

#5*5
ksize1 = 5
ker_x1 = [np.ones(ksize1)]
ker_y1 = np.transpose(ker_x1)

ker_blur1 = ker_y1*ker_x1
ker_blur1 = np.uint8(ker_blur1)/(ksize1*ksize1)

print(ker_blur1)
res1 = cv2.filter2D(img,0,ker_blur1)

#9*9
ksize2 = 9
ker_x2 = [np.ones(ksize2)]
ker_y2 = np.transpose(ker_x2)

ker_blur2 = ker_y2*ker_x2
ker_blur2 = np.uint8(ker_blur2)/(ksize2*ksize2)

print(ker_blur2)
res2 = cv2.filter2D(img,0,ker_blur2)

#15*15
ksize3 = 15
ker_x3 = [np.ones(ksize3)]
ker_y3 = np.transpose(ker_x3)

ker_blur3 = ker_y3*ker_x3
ker_blur3 = np.uint8(ker_blur3)/(ksize3*ksize3)

print(ker_blur3)
res3 = cv2.filter2D(img,0,ker_blur3)

#25*25
ksize4 = 25
ker_x4 = [np.ones(ksize4)]
ker_y4 = np.transpose(ker_x4)

ker_blur4 = ker_y4*ker_x4
ker_blur4 = np.uint8(ker_blur4)/(ksize4*ksize4)

print(ker_blur4)
res4 = cv2.filter2D(img,0,ker_blur4)

cv2.imshow("original",img)
cv2.imshow("Blur1",res1)
cv2.imshow("Blur2",res2)
cv2.imshow("Blur3",res3)
cv2.imshow("Blur4",res4)

cv2.waitKey(0)
cv2.destroyAllWindows()