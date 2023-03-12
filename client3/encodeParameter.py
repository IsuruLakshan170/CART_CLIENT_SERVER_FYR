#Encoding and decoding model parameters

import base64
import modelGenerator as mg
import modelAccuracy as ma
import dataSetSplit as sp
import pickle
import os



def encodeModelParameters():
    # x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()

    print("Encoding ----------------> ")
    model = mg.create_model()
    model.load_weights('backup/model_weights.h5')
     # Get the size of the saved model weight file
    # model_size_bytes = os.path.getsize('modelData/model_weights.h5')
    # # Convert bytes to MB
    # model_size_mb = model_size_bytes / (1024 * 1024)

    # print(f"The size of the  model parameters is {model_size_mb:.2f} MB.")
    # ma.getModelAccuracy(model,x_test_np,y_test_np)
    receivedModelParameters  = model.get_weights()
    
    #encode the model
    model_by= pickle.dumps(receivedModelParameters)
    encoded_message =base64.b16encode(model_by)
    #convert to string
    my_string = encoded_message.decode("utf-8")

    # print(type(my_string))
    print("Size of encoded model parameter is (String Data type): {:.2f} MB".format(len(my_string) / (1024 * 1024)))

    # print("Return encoded parameters as string")
    return my_string

def decodeModelParameters(encoded_message):
    directory = "receivedModelParameter" #replace with your directory path
    num_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    num_files =num_files+1
    # x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()

    print("Decoding ----------------> ")
    #decode the model
    # print(type(encoded_message))
    my_bytes = encoded_message.encode("utf-8")
    # print(type(my_bytes))
    decode_b64 = base64.b16decode(my_bytes)
    decode_model_weights=pickle.loads(decode_b64)
   
    model = mg.create_model()
    model.set_weights(decode_model_weights)
    # ma.getModelAccuracy(model,x_test_np,y_test_np)
    model.save_weights(f'receivedModelParameter/model_weights_{num_files}.h5')
    
    return decode_model_weights



# #encode the model weights 
# encodedData = encodeModelParameters()
# #decode the model weights
# decodeModelParameters(encodedData)

