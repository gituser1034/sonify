import cv2 as cv

# Loading in a video
path = "Hurricane Visualization.webm"
capture = cv.VideoCapture(path)

# While loop and read video frame by frame
while True:
    ret, frame = capture.read()
    cv.imshow("Video", frame)

    # If d is pressed stop video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)