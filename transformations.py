import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)


# Transformation
# def translate(img, x, y):
#     transMat = np.float32([[1, 0, x], [0, 1, y]])
#     dimentions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimentions)
#
# # -x --> Left
# # -y --> Up
# # x --> Right
# # y --> Down
#
#
# translated = translate(img, 20, 20)
# cv.imshow("Translated", translated)

# # Rotation
# def rotate(img, angle, rotPoint = None):
#     (height, width)= img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
#
#     rotMat = cv.getRotationMatrix2D(rotPoint, -angle, 1.0)
#     dimensions = (width, height)
#     return cv.warpAffine(img, rotMat, dimensions)
#
# rotated = rotate(img, 45)
# cv.imshow("Rotated", rotated)
#
# rotated_rotated = rotate(rotated, 45)
# cv.imshow("Rotated_rotated", rotated_rotated)

# # Resizing
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)


# # Flipping
# flip = cv.flip(img, 0)
# # 0: Flip theo chieu doc vertical
# # 1: Flip theo chieu nhang Horizontal
#
# cv.imshow("Flipped", flip)


# Cropping
cropped = img[50:400, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)