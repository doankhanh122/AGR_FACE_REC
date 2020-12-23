import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Edge", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow("Contours Draw", blank)

cv.waitKey(0)
