import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
# set function need resolution supported by camera only
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    success, img = cap.read()
    # img = cv2.resize(img, (frameWidth, frameHeight))  #resize function you can give any resolution
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break