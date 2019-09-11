import cv2
from psonic import *


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color thresholds extracted from testing [Off, On, Note]
    # This will let you play Hot Cross Buns Trio
    green = [(), (), 'D4']
    red = [(), (), 'G4']
    blue = [(), (), 'A4']
    yellow = [(), (), 'B4']
    white = [(), (), 'C4']

    colors = [green, red, blue, yellow, white]
    
    # Dectect lit LEDs 
    for color in colors:

        # Create a mask for the color
        mask = cv2.inRange(hsv_frame, colors[color][0], colors[color][1])
        
        # Check if mask isn't black
        if list(mask) != list(mask)[:-1]:
            play(color[2], release = 0.1)

# When everything done, release the capture
cap.release()