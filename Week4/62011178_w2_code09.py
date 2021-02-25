import cv2
import numpy as np

img = cv2.imread("dataset/coins.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,
                            dp=1.0,
                            minDist=15,
                            param1=100,
                            param2=60,
                            minRadius=40,
                            maxRadius=70)

print(len(circles))
print("Before around : ",circles[0])
circles = np.uint16(np.around(circles))
print("After around : ",circles[0])
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),thickness=3)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),thickness=3)
cv2.imshow("gray",gray)
cv2.imshow("Circle detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()