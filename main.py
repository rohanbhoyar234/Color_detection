import cv2
from PIL import  Image
from util import get_limits

yellow = [0,255,255] # yellow color in BGR colorspace


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage,lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bounding_box = mask_.getbbox()
    # print(bounding_box)

    if bounding_box is not None:
        x1,y1,x2,y2 = bounding_box
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)

    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()