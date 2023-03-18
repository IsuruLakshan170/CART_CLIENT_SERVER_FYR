#Encoding and decoding model parameters

import base64
import modelGenerator as mg
import os
import zlib
import numpy as np
import io


def encodeModelParameters():
   
    print("Encoding ----------------> ")
    model = mg.create_model()
    model.load_weights('backup/model_weights.h5')

    model_weights = model.get_weights()

    # save the model weights to an in-memory buffer
    buf = io.BytesIO()
    np.savez(buf, *model_weights)
    model_bytes = buf.getvalue()

    # compress the serialized weights
    compressed_model = zlib.compress(model_bytes)

    # encode the compressed data as a base64 string
    # my_string = base64.b64encode(compressed_model).decode('utf-8')

    print("Size of encoded model parameter is (Byte Data type): {:.2f} MB".format(len(compressed_model) / (1024 * 1024)))
    print(type(compressed_model))

    # print("Return encoded parameters as string")
    return compressed_model

#decode parameters
def decodeModelParameters(encoded_message):
    print("Start decoding ----------------> ")
    directory = "receivedModelParameter" #replace with  directory path
    num_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    num_files =num_files+1

    # decode the base64 string and decompress the data
    # compressed_model = base64.b64decode(encoded_message.encode('utf-8'))
    model_bytes = zlib.decompress(encoded_message)

    # load the model parameters from the serialized data
    with np.load(io.BytesIO(model_bytes)) as data:
        model_weights = [data[f'arr_{i}'] for i in range(len(data.files))]

    model = mg.create_model()
    # set the model parameters to the loaded values
    model.set_weights(model_weights)
    model.save_weights(f'receivedModelParameter/model_weights_{num_files}.h5')
    print(f'Decode completed and save Received model parameter {num_files}')
    return model_weights
