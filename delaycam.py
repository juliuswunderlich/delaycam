import cv2
import threading
import time

cap = cv2.VideoCapture(0)
queue = []
DELAY_DURATION = 5 #in seconds

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def producer():
    global queue
    global cap
    while True:
        ret, frame = cap.read()
        #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        queue.append(frame)

producerThread = threading.Thread(target=producer)
producerThread.start()

while True:
    if len(queue) < 30 * DELAY_DURATION:
        continue
    print(len(queue))
    frame = queue.pop(0)
    cv2.imshow('Video Stream', frame)

    # waitKey required
    c = cv2.waitKey(1)
    if c == 27:
        break