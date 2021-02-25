# Histogram graph

from cv2 import cv2
from matplotlib import pyplot as plot

img = cv2.imread("dataset/graylevel.jpg")
full_His = cv2.calcHist([img],[0],None,[256],[0,256])

cv2.imshow("Gray level",img)
plot.plot(full_His)
plot.show()

cv2.waitKey(0)
cv2.destroyAllWindows()