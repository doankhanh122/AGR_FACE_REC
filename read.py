import cv2 as cv


# Reading image
################
# img = cv.imread('Photos/cat2.jpg')
# cv.imshow("Cat", img)


# Reading video
################
# capture = cv.VideoCapture(0) for webcam
capture = cv.VideoCapture("Videos/video2.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)