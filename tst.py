import cv2 as cv
import numpy as np

path = "sonify_galactic.jpg"
img = cv.imread(path)

grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Vertical position = which row you're on, need number of rows
print(grayImg.shape)

cv.imshow("Image Test", grayImg)

# Displays image until a key is pressed
cv.waitKey(0)