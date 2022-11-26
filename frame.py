import cv2
import os

vidcap = cv2.VideoCapture('chase.mp4') 
os.chdir("frames/")

frame = 0
i = 1

while 5:
    ret, img = vidcap.read()
    frame = frame + 1

    if frame == 5:
        cv2.imwrite('dt4_'+str(i)+'.jpg', img)
        i = i+1
        frame = 0
 

  