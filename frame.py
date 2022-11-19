import cv2
import os

vidcap = cv2.VideoCapture('chase.mp4') 
os.chdir("frame/")

wait = 0
i = 1

while 5:
    ret, img = vidcap.read()
    wait = wait+100

    if wait == 1000:
        cv2.imwrite('data_'+str(i)+'.jpg', img)
        i = i+1
        wait = 0
 

  