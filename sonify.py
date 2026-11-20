# Run venv
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
path = "Pillars of Creation.png"
img = cv.imread(path)

# Converting image data to grayscale
# This is a 2D arr of pixel intensities
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Pitch mapping
# Want to convert a pixel intensity (int from 0 - 255) to a musical note

# MIDI nummbers are the numerical value to letter keys like C# or something
# Piano range (21–108): A standard 88-key piano starts at MIDI number 21 (the lowest A) and ends 
# at 108 (the highest C). Middle C (C4) is 60. You convert names to MIDI numbers because computers 
# and audio libraries prefer working with clean integers like 60 rather than text strings like "C4".

# Great resolution: Across 3 octaves, all white keys give you 21 or 22 distinct notes across 0–255 
# (roughly one note per 12 intensity levels), which is enough to clearly hear 
# gradients without overwhelming your ears.
# Essentially if we have 0,1,2 this can just be noise, so little difference, intensity
# 0-12 may all look the same, so want it to have the same note
# using the whole piano doesn't allow a good split like using a few octaves of c major
# c major is c to another c, only white keys, sounds best to me for this

# pitch = vertical location, higher up = higher pitch
# pixel intensity = volume

# Choosing notes = choosing pitch, maps to pixel location
# Starting with C major, 3 octaves, C2 to B4
# MIDI number for C2 = 36 (low), B4 = 56 (high)
notes = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 
         'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 
         'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Need to normalize vertical pixel locations to 36 - 56 scale. 


# Show image
# Pass in name of window and the image matrix
cv.imshow("Image Test", grayImg)

# Displays image until a key is pressed
cv.waitKey(0)

