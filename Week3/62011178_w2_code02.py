import cv2
import numpy as np

img = cv2.imread("dataset/coins.jpg")

#1
sigma1 = 1.4
ksize1 = 5
ker_gaux1 = cv2.getGaussianKernel(ksize1,sigma1)
ker_gauy2 = np.transpose(ker_gaux1)

ker_gau1 = ker_gaux1*ker_gauy2


print(ker_gau1)
res1 = cv2.filter2D(img,0,ker_gau1)

#2
sigma2 = 3.2
ksize2 = 5
ker_gaux2 = cv2.getGaussianKernel(ksize2,sigma2)
ker_gauy2 = np.transpose(ker_gaux2)

ker_gau2 = ker_gaux2*ker_gauy2


print(ker_gau2)
res2 = cv2.filter2D(img,0,ker_gau2)

#3
sigma3 = 1.4
ksize3 = 7
ker_gaux3 = cv2.getGaussianKernel(ksize3,sigma3)
ker_gauy3 = np.transpose(ker_gaux3)

ker_gau3 = ker_gaux3*ker_gauy3


print(ker_gau3)
res3 = cv2.filter2D(img,0,ker_gau3)

#4
sigma4 = 3.2
ksize4 = 7
ker_gaux4 = cv2.getGaussianKernel(ksize4,sigma4)
ker_gauy4 = np.transpose(ker_gaux4)

ker_gau4 = ker_gaux4*ker_gauy4


print(ker_gau4)
res4 = cv2.filter2D(img,0,ker_gau4)

cv2.imshow("original",img)
cv2.imshow("Gaussian result size =" + str(ksize1) + " Sigma =" + str(sigma1),res1)
cv2.imshow("Gaussian result size =" + str(ksize2) + " Sigma =" + str(sigma2),res2)
cv2.imshow("Gaussian result size =" + str(ksize3) + " Sigma =" + str(sigma3),res3)
cv2.imshow("Gaussian result size =" + str(ksize4) + " Sigma =" + str(sigma4),res4)


cv2.waitKey(0)
cv2.destroyAllWindows()