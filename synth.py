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
    green = [(1,88,48 ), (3,115,71), 'D4']
    red = [(160,0,0), (200,3,25), 'G4']
    blue = [(0,0,253), (0,0,255), 'A4']
    yellow = [(250,200,0), (255,255,1), 'B4']
    white = [(), (), 'C4'] # this one is very problematic since all LEDs have some white, may have to do a volume measurement
     

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