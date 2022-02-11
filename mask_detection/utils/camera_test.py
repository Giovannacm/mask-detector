from imutils.video import VideoStream
from picamera import PiCamera
from time import sleep
import cv2

camera = VideoStream(usePiCamera=True).start()
sleep(1.0)
in_loop = True

while in_loop:
    ret, frame = camera.read(), camera.read()
    cv2.rectangle(frame, (50, 50), (90, 90), (0, 255, 0), 2)
    cv2.imshow("Video", frame)
    
    key = cv2.waitKey(1) & 0xFF == ord('q')
    if key:
        in_loop = False
    
cv2.destroyAllWindows()
camera.stop()