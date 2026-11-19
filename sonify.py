# Run venv
# python3 -m venv .venv
# source .venv/bin/activate
# pip install opencv-python numpy scipy sounddevice
# pip install opencv-python numpy audiolazy
# deactivate

import cv2 as cv
import numpy as np
# Gemini saying sounddevice for real time playback
# I think either scipy or soundfile for creating full on audio output files
# import sounddevice as sd
# Trying audiolazy like the video first
from audiolazy import str2midi

# Chatgpt saying this about making a function to control everything between the darkest and
# brightest pixels
# You only have to decide two bounds—what 0 (black) maps to and what 255 (white)
# maps to—and how the numbers in between behave.

# Load in an image with opencv
path = "Pillars of Creation.png"
img = cv.imread(path)

# Want to convert the image to grayscale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Using musical notes for pitch mapping from audiolazy
str2midi('C3')



# Show image
# Pass in name of window and the image matrix
cv.imshow("Image Test", grayImg)

# Displays image until a key is pressed
cv.waitKey(0)

