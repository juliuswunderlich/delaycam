import cv2
import threading
import time

cap = cv2.VideoCapture(0)
queue = []
DELAY_DURATION = 5 #in seconds
SLOW_MO_AMOUNT = 1 # ramp this up to achieve somewhat of slowmotion

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def producer():
    global queue
    global cap
    while True:
        ret, frame = cap.read()
        #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        if len(queue) < int(30 * DELAY_DURATION):
            queue.append(frame)

producerThread = threading.Thread(target=producer)
producerThread.start()

while True:
    if len(queue) < int(30 * DELAY_DURATION):
        continue
    frame = queue.pop(0)
    cv2.imshow('Video Stream', frame)

    # waitKey required
    if cv2.waitKey(SLOW_MO_AMOUNT) & 0xFF == ord('q'):
        break
