import signal
import sys
import time
from soc9k import peerCom
from enumList import conctionType
from com import communicationProx
from seed import seedProx

import encodeParameter

HOST = 'localhost'  #'13.250.112.193'
PORT = 9000
CURRENT_PROCESS = "HOLD"
########################################################################
#------------------------------PEER   DATA-----------------------------#
# MODELPARAMETERS  = "Model 3"
MODELPARAMETERS = encodeParameter.encodeModelParameters()

# MODELPARAMETERS  = bytes(1024)  # 1 KB
# MODELPARAMETERS  = bytes(100*1024)  # 100 KB
# MODELPARAMETERS  = bytes(1024*1024)  # 1 MB
# MODELPARAMETERS  = bytes(3*1024*1024)  # 3 MB
# MODELPARAMETERS  = bytes(5*1024*1024)  # 5 MB
########################################################################

########################################################################
#------------------------------MOBILE MODEL----------------------------#
MOBILEMODELPARAMETERS  = bytes(1024)  # 1 KB
########################################################################

def sigint_handler(signal, frame, mySocket):
    print('Exiting program...')
    mySocket.close(0)
    sys.exit(0)

def mainFunn(MODE, RECIVER_TIMEOUT ,TIMEOUT = 12, SYNC_CONST = 1):
    mySocket = peerCom(HOST, PORT, TIMEOUT , MODE, SYNC_CONST)
    signal.signal(signal.SIGINT, lambda signal, frame: sigint_handler(signal, frame, mySocket))
    USERID = mySocket.connect()
    mySocket.start_receiver()
    mySocket.start_sender()
    print("USER TYPE  : ",MODE)
    print("USER ID    : ",USERID)
    if MODE == conctionType.KERNEL.value:
        MODELPARAMETERLIST = communicationProx(mySocket,USERID,MODE,RECIVER_TIMEOUT,MODELPARAMETERS)
        print("LIST")
        print("length : ",len(MODELPARAMETERLIST))
        for item in MODELPARAMETERLIST:
            if "MODELPARAMETERS" in item['Data']:
                receivedData = item['Data'][1]
                # print(receivedData)
                encodeParameter.decodeModelParameters(receivedData)
                
    if MODE == conctionType.SHELL.value:
        seedProx(mySocket,USERID,MODE,MOBILEMODELPARAMETERS,MODELPARAMETERS,RECIVER_TIMEOUT)

def connectNetwork(type):
    if type == "SHELL":
        if __name__ == "__main__":
            mainFunn("SHELL",30)
            time.sleep(2)
            print("loop call triggered")
  
    elif type == "KERNEL":
        if __name__ == "__main__":
            mainFunn("KERNEL",15)
            time.sleep(2)
            print("loop call triggered")



def kernelProcess(type):
    global CURRENT_PROCESS
    while True:
        if CURRENT_PROCESS == "HOLD":
            CURRENT_PROCESS = "KERNEL"
            connectNetwork(type)
            CURRENT_PROCESS ="HOLD"
            break 
        else:
            time.sleep(20)
               
def shellProcess(type):
    global CURRENT_PROCESS
    while True:
        if CURRENT_PROCESS == "HOLD":
            CURRENT_PROCESS = "SHELL"
            connectNetwork(type)
            CURRENT_PROCESS ="HOLD"
            time.sleep(5)
        else:
            time.sleep(20)

# kernelProcess("KERNEL")
shellProcess("SHELL")