import cv2 as cv
import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal
# don't work with wsl
import sounddevice as sd

sample_rate, data = wav.read("stereol.wav")

# print(sample_rate)
# # 2 dimensions indicates stereo format - standard for most audio, left and right channel
# print(data.shape)
# print(data.dtype)

sd.play(data)