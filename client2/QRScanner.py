import cv2
from pyzbar.pyzbar import decode
import writeFile as wf


def QRReader():
    cam = cv2.VideoCapture(0)
    cam.set(5,640)
    cam.set(6,480)

    camera = True
    while camera == True:
        suceess,frame = cam.read()
        
        for i in decode(frame):
          
            decodeItem =i.data.decode('utf-8')
            print(decodeItem)
            return decodeItem
            
          