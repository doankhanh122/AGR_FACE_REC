import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)

plt.imshow(img)
plt.show()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Hsv", hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)


cv.waitKey(0)