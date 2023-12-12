import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250, 350  # actual width and height of the card in mm
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])  # pixel coordinates on the image
                                                                    # (we can get it by loading the image in paint)
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # actual 2d image pixel coordinates
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)
