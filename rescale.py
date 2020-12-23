import cv2 as cv


# Function rescale Frame
def rescaleFrame(frame, scale = 0.75):
    # Images, Videos and Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Function change Resolution
def changeRes(width, height):
    # Only work with Live video
    capture.set(3, width)
    capture.set(4, height)


# Rescale image
################
img = cv.imread('Photos/cat2.jpg')


resized_img = rescaleFrame(img, scale=.2)
cv.imshow("Cat", resized_img)
# Reading video
################
# capture = cv.VideoCapture(0) for webcam
capture = cv.VideoCapture("Videos/video2.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    # cv.imshow("Video", frame)
    cv.imshow("Video resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
