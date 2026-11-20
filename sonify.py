# Run venv - as of now don't need the venv as not using any sound library
# python3 -m venv .venv
# source .venv/bin/activate
# pip install opencv-python numpy scipy sounddevice (older)
# deactivate

# Gonna try note conversion in regular python, no libraries

import cv2 as cv
import numpy as np

# Gemini saying sounddevice for real time playback
# I think either scipy or soundfile for creating full on audio output files

# Chatgpt saying this about making a function to control everything between the darkest and
# brightest pixels
# You only have to decide two bounds—what 0 (black) maps to and what 255 (white)
# maps to—and how the numbers in between behave.

# Load in an image with opencv
path = "pillars.jpg"
img = cv.imread(path)

# Converting image data to grayscale
# This is a 2D arr of pixel intensities
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

shape = grayImg.shape
# Vertical position/height = which row you're on, 0 = top row of image
height = shape[0]
width = shape[1]

# Pitch mapping

# MIDI nummbers are the numerical value to letter keys like C# or something
# Piano range (21–108): A standard 88-key piano starts at MIDI number 21 (the lowest A) and ends 
# at 108 (the highest C). Middle C (C4) is 60. You convert names to MIDI numbers because computers 
# and audio libraries prefer working with clean integers like 60 rather than text strings like "C4".

# using the whole piano doesn't allow a good split like using a few octaves of c major
# c major is c to another c, only white keys, sounds best to me for this
# A picture is large, many vertical positions ie 500, 0,1,2 is just noise, can map to the 
# same pitch, need to divide the pitches to cover the whole range

# pitch = vertical location, higher up = higher pitch
# pixel intensity (0-255) = volume
# Time = left to right

# Choosing notes = choosing pitch, maps to pixel location
# Starting with C major, 3 octaves, C2 to B4
# MIDI number for C2 = 36 (low), B4 = 56 (high)
notes = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 
         'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 
         'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Need to normalize vertical pixel locations to 36 - 56 scale.

# Testing straight up frequencies first


# Show image
# Pass in name of window and the image matrix
cv.imshow("Image Test", grayImg)

# Displays image until a key is pressed
cv.waitKey(0)

