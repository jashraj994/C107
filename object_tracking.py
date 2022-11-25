import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()

returned,img = video.read()

ball = cv2.selectROI("tracking",img,False)
tracker.init(img,ball)
print(ball) 

def drawBox(img,ball):
    x,y,w,h = int(ball[0]), int(ball[1]), int(ball[2]), int(ball[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,255,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img,ball):
    x,y,w,h = int(ball[0]), int(ball[1]), int(ball[2]), int(ball[3])


while True:
    check,img = video.read()   
    success,ball = tracker.update(img)

    if success:
        drawBox(img,ball)
       
    else:

        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



