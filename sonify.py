# Create venv:
# python3 -m venv .venv
# source .venv/bin/activate
# pip install opencv-python numpy scipy sounddevice
# sudo apt update
# sudo apt install libportaudio2 portaudio19-dev (this needed for sounddevice library)
# deactivate

# Gonna try note conversion in regular python, no libraries

import cv2 as cv
import numpy as np
import scipy.io.wavfile as wave
import scipy.signal as signal

# Scipy creates wav files, sounddevice allows audio playback within program (may not need)

# Load in an image with opencv
path = "pillars.jpg"
img = cv.imread(path)

# Converting image data to grayscale
# This is a 2D arr of pixel intensities
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# (860, 864) - Height x Width
shape = grayImg.shape
# Vertical position/height = which row you're on, 0 = top row of image
height = shape[0]
width = shape[1]

# pitch = vertical location, higher up = higher pitch
# volume = pixel intensity (0-255)
# Time = left to right

# Testing straight up frequencies first - 150 hz to 4186 (then gonna try 3000 and adjust so its comfortable)

# Generate an array from 150hz to 4186hz, logarithmic scale (hearing is logarithmic, smooth pitch scaling)
# the same length as the original image 
pitches = np.geomspace(150, 4186, num=height)
# Reverse as top of image is row 0
pitches_rev = pitches[::-1]

# Map pixel intensity to volume - volume works with amplitdue from 0-1
# just normalize each pixel from 0 - 1, 255 mapped to 1 so divide everything by 255 
# (255 / 255 = 1)
volume = grayImg / 255

# Now I have a pitch array, and a volume 2D array
# Somehow combining the pitch and volume per column
# For each element in a column will have a wave, add all these waves together
# so a column has one combined wave
# Do this for each column
# Should have a final 1D arr of these wave values
# Can output this to a .wav file and play the audio

# 44,100 Hz, Default sample rate common for audio
sample_rate = 44100

# Time, left to right?

# playback for actual sound?????

# Show image
# Pass in name of window and the image matrix
cv.imshow("Image Test", grayImg)

# Displays image until a key is pressed
cv.waitKey(0)

