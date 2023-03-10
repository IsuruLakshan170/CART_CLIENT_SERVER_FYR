import cv2
from pyzbar.pyzbar import decode
import time
import writeFile as wf
import requests
import Flask
import threading

def QRReader():
    cam = cv2.VideoCapture(0)
    cam.set(5,640)
    cam.set(6,480)

    camera = True
    while camera == True:
        suceess,frame = cam.read()
        
        for i in decode(frame):
            # print(i,type)
            decodeItem =i.data.decode('utf-8')
            print(decodeItem)
            return decodeItem
            # month = 3
            # item = decodeItem
            # gender = 0
            # if decodeItem in "Item 1" :
            #     item = 1
                
            #     # wf.writetoCSV(month, item, gender)
            #     # url = 'http://127.0.0.1:5000/getItems'
            #     # data = {'res': 55}
            #     # response = requests.post(url, data=data)
            #     # print(response.text)
            # elif decodeItem in "Item 2" :
            #     item = 2
            #     # wf.writetoCSV(month, item, gender)
            #     # Flask.getItems()
            time.sleep(6)
            # return decodeItem
        
    # return decodeItem
        # cv2.imshow("QR Scanner",frame)
        # cv2.waitKey(3)

