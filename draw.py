import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8") #width, height, number channel colour
# cv.imshow("Blank", blank)
#
# img = cv.imread("Photos/cat.jpg")
# cv.imshow("Cat", img)


# 1. Paint the image a certain colour
# blank[:] = 0,255,0
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Red", blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) # border = 2
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) # solid color  or thickness = -1
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED) # make square
# cv.imshow("Rectangle", blank)

# 3. Draw circle
# cv.circle(blank, (250, 250), 100, (0,255,255), thickness=-1)
# cv.imshow("Yellow Circle", blank)

# 4. Draw a line
# cv.line(blank, (0, 0), (blank.shape[1]//2,blank.shape[0]//2), (0, 0, 255), thickness=2)
# cv.imshow("Red line", blank)

# 5. Write text
cv.putText(blank, "Doan Khanh", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), thickness=2)
cv.imshow("Text", blank)




cv.waitKey(0)