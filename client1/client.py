# import signal
# import sys
# import time
# from soc9k import peerCom
# from enumList import conctionType
# from com import communicationProx
# from seed import seedProx
# import pandas as pd
import encodeParameter
# import Main 
# import os

# HOST = 'localhost'  #'13.250.112.193'
# PORT = 9000
# ########################################################################
# #------------------------------PEER   DATA-----------------------------#
# # MODELPARAMETERS  = "Model 2"
# MODELPARAMETERS = encodeParameter.encodeModelParameters()

# # MODELPARAMETERS  = bytes(1024)  # 1 KB
# # MODELPARAMETERS  = bytes(100*1024)  # 100 KB
# # MODELPARAMETERS  = bytes(1024*1024)  # 1 MB
# # MODELPARAMETERS  = bytes(3*1024*1024)  # 3 MB
# # MODELPARAMETERS  = bytes(5*1024*1024)  # 5 MB
# ########################################################################

# ########################################################################
# #------------------------------MOBILE MODEL----------------------------#
# MOBILEMODELPARAMETERS  = bytes(1024)  # 1 KB
# ########################################################################

# def sigint_handler(signal, frame, mySocket):
#     print('Exiting program...')
#     mySocket.close(0)
#     sys.exit(0)

# def mainFunn(MODE, RECIVER_TIMEOUT ,TIMEOUT = 12, SYNC_CONST = 1):
#     mySocket = peerCom(HOST, PORT, TIMEOUT , MODE, SYNC_CONST)
#     signal.signal(signal.SIGINT, lambda signal, frame: sigint_handler(signal, frame, mySocket))
#     USERID = mySocket.connect()
#     mySocket.start_receiver()
#     mySocket.start_sender()
#     print("USER TYPE  : ",MODE)
#     print("USER ID    : ",USERID)
#     if MODE == conctionType.KERNEL.value:
#         MODELPARAMETERLIST = communicationProx(mySocket,USERID,MODE,RECIVER_TIMEOUT,MODELPARAMETERS)
#         print("LIST")
#         print("length : ",len(MODELPARAMETERLIST))
#         for item in MODELPARAMETERLIST:
#             if "MODELPARAMETERS" in item['Data']:
#                 receivedData = item['Data'][1]
#                 # print(receivedData)
#                 encodeParameter.decodeModelParameters(receivedData)
                
#     if MODE == conctionType.SHELL.value:
#         seedProx(mySocket,USERID,MODE,MOBILEMODELPARAMETERS,MODELPARAMETERS,RECIVER_TIMEOUT)


       
# def connectNetwork(type):
#     if type == "SHELL":
#             mainFunn("SHELL",50)
#             time.sleep(2)
#             print("loop call triggered")

#     elif type == "KERNEL":
#             mainFunn("KERNEL",15)
#             time.sleep(2)
#             print("loop call triggered")


# #----------------------background process --------------------------------
# def backgroudNetworkProcess():
#       while True:
#             directoryModelData = "backup" 
#             modelDataSize = len([f for f in os.listdir(directoryModelData) if os.path.isfile(os.path.join(directoryModelData, f))])
#             cartData = pd.read_csv('dataset/cartData.csv')
#             #if cart is new 
#             if modelDataSize == 0:
#                  print("Initializing cart")
#                  while True:
#                     directoryReceivedParameters = "receivedModelParameter" 
#                     receivedParametersSize = len([f for f in os.listdir(directoryReceivedParameters) if os.path.isfile(os.path.join(directoryReceivedParameters, f))])
#                     #check received parameters size 
#                     if receivedParametersSize >= 4:
#                         Main.initialAggregationProcess()
#                         break
#                     else:
#                         connectNetwork("KERNEL") 
            
                
#             #compare size of the dataset for globla aggregation
#             elif len(cartData) >= 3:
#                 print("Connecting as KERNEL for globla aggregation")
#                 while True:
#                     directoryReceivedParameters = "receivedModelParameter" 
#                     receivedParametersSize = len([f for f in os.listdir(directoryReceivedParameters) if os.path.isfile(os.path.join(directoryReceivedParameters, f))])
#                     #check received parameters size 
#                     if receivedParametersSize >= 4:
#                         Main.globleAggregationProcess()
#                         break
#                     else:
#                         connectNetwork("KERNEL") 
            
#             else:
#                 print("Connecting as SHELL for send Models")
#                 connectNetwork("SHELL")
            
#             time.sleep(5)  
        

import random
import signal
import sys
import sys
import time
import os
from soc9k import peerCom
from enumList import conctionType
from com import communicationProx
from seed import seedProx
from file import getID
import Main 
import encodeParameter
import pandas as pd

HOST = '141.145.200.6' #141.145.200.6
PORT = 9000

########################################################################
#------------------------------PEER   DATA-----------------------------#
MODELPARAMETERS = encodeParameter.encodeModelParameters()
# MODELPARAMETERS  = bytes(1024)  # 1 KB
# MODELPARAMETERS  = bytes(100*1024)  # 100 KB
# MODELPARAMETERS  = bytes(1024*1024)  # 1 MB
# MODELPARAMETERS  = bytes(3*1024*1024)  # 3 MB
# MODELPARAMETERS  = bytes(5*1024*1024)  # 5 MB
########################################################################

########################################################################
#------------------------------MOBILE MODEL----------------------------#
# MOBILEMODELPARAMETERS  = "jhjhhkhkhkl"
# MOBILEMODELPARAMETERS  = bytes(1024)  # 1 KB
# MOBILEMODELPARAMETERS  = bytes(1024*1024)  # 1 MB
# MOBILEMODELPARAMETERS  = bytes(5*1024*1024)  # 5 MB
MOBILEMODELPARAMETERS  =encodeParameter.encodeModelParametersForMobile()

########################################################################a

def sigint_handler(signal, frame, mySocket, USERID):
    print('Exiting program...')
    mySocket.close(0,USERID)
    sys.exit(0)

def mainFunn(MODE,RECIVER_TIMEOUT, TIMEOUT = 12, SYNC_CONST = 1):
    try:
        mySocket = peerCom(HOST, PORT, TIMEOUT , MODE, SYNC_CONST)
        signal.signal(signal.SIGINT, lambda signal, frame: sigint_handler(signal, frame, mySocket, USERID))
        TEMPUSERID = mySocket.connect()
        USERID = getID(TEMPUSERID)
        mySocket.start_receiver()
        mySocket.start_sender()
        print("USER TYPE  : ",MODE)
        if MODE == conctionType.KERNEL.value:
            MODELPARAMETERLIST = communicationProx(mySocket,TEMPUSERID,MODE,RECIVER_TIMEOUT,MODELPARAMETERS,USERID)
            print("LIST")
            print("length : ",len(MODELPARAMETERLIST))
            for item in MODELPARAMETERLIST:
                if "MODELPARAMETERS" in item['Data']:
                    receivedData = item['Data'][1]
                    # print(receivedData)
                    encodeParameter.decodeModelParameters(receivedData)
                    
        if MODE == conctionType.SHELL.value:
            seedProx(mySocket,TEMPUSERID,MODE,MOBILEMODELPARAMETERS,MODELPARAMETERS,RECIVER_TIMEOUT,USERID)
    
    except Exception as e:
        print("Error occurred while running in", MODE, " mode ")

# #Call from Separat thread
# if __name__ == "__main__":
#     while True:
#         randomNo= random.randint(0, 50)
#         if randomNo > 15:
#             mainFunn("SHELL")
#         else:
#             mainFunn("KERNEL")
#         time.sleep(randomNo)


    
def connectNetwork(type):
    if type == "SHELL":
            mainFunn("SHELL",50)
            time.sleep(2)
            print("loop call triggered")

    elif type == "KERNEL":
            mainFunn("KERNEL",30)
            time.sleep(2)
            print("loop call triggered")


#----------------------background process --------------------------------
def backgroudNetworkProcess():
      while True:
            directoryModelData = "backup" 
            modelDataSize = len([f for f in os.listdir(directoryModelData) if os.path.isfile(os.path.join(directoryModelData, f))])
            cartData = pd.read_csv('dataset/cartData.csv')
            #if cart is new 
            if modelDataSize == 0:
                 print("Initializing cart")
                 while True:
                    directoryReceivedParameters = "receivedModelParameter" 
                    receivedParametersSize = len([f for f in os.listdir(directoryReceivedParameters) if os.path.isfile(os.path.join(directoryReceivedParameters, f))])
                    #check received parameters size 
                    if receivedParametersSize >= 4:
                        Main.initialAggregationProcess()
                        break
                    else:
                        connectNetwork("KERNEL") 
            
                
            #compare size of the dataset for globla aggregation
            elif len(cartData) >= 3:
                print("Connecting as KERNEL for globla aggregation")
                while True:
                    directoryReceivedParameters = "receivedModelParameter" 
                    receivedParametersSize = len([f for f in os.listdir(directoryReceivedParameters) if os.path.isfile(os.path.join(directoryReceivedParameters, f))])
                    #check received parameters size 
                    if receivedParametersSize >= 4:
                        Main.globleAggregationProcess()
                        break
                    else:
                        connectNetwork("KERNEL") 
            
            else:
                print("Connecting as SHELL for send Models")
                connectNetwork("SHELL")
            
            time.sleep(5)  
        

