import cv2
import threading
import time

cap = cv2.VideoCapture(0)
queue = []
isFirstTime = True
allowed = True
DELAY_DURATION = 10 #in seconds

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
        #time.sleep(1)
        continue
    frame = queue.pop(0)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break