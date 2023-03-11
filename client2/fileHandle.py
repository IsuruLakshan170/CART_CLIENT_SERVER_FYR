import requests
import os

#download files from internet
def downloadFile(url,filename):
    try:
        with requests.get(url) as req:
            with open(filename,'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


downloadLink = 'https://thumbs.dreamstime.com/z/close-up-inside-okra-flowe-45588243.jpg'
# downloadFile(downloadLink,'downloads/testImage.jpg')

#removefile from receivedModelParameter
def removeFiles():
    for i in range(5):
        num=i+1
        path = f'receivedModelParameter/model_weights_{num}.h5'
        try:
             os.remove(path)
        except FileNotFoundError:
             print("That file does not exist")
    print("Model parameters are removed from the local filesystem")

#remove the file from the initModelParameters
def removeInitFiles():
    directory = "receivedModelParameter" #replace with your directory path
    num_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    for i in range(num_files):
        num=i+1
        path = f'receivedModelParameter/model_weights_{num}.h5'
        try:
             os.remove(path)
        except FileNotFoundError:
             print("That file does not exist")
    print("Model parameters are removed from inital model parameter folder the local filesystem")

