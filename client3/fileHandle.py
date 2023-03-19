import os

#remove the file from the initModelParameters
def removeFiles():
    directory = "receivedModelParameter" #replace with your directory path
    num_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    for i in range(num_files):
        num=i+1
        path = f'receivedModelParameter/model_weights_{num}.h5'
        try:
             os.remove(path)
        except FileNotFoundError:
             print("That file does not exist")
    print("Model parameters are removed from receivedModelParameter folder ")
