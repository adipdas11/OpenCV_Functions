import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

# Convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BLur the image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) #(7,7) is called kernal  and can be odd num. only increasing it will increase blur

# edge detection (vary 150 and 200 which are threshold to get more edges or less edge detection)
imgCanny = cv2.Canny(img, 150, 200)

# increase the thickness of the edge detection by canny
# change in iteration effects the thickness
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# reverse of dialation decrease the thickness of edges
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)