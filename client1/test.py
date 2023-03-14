import base64
import modelGenerator as mg
import modelAccuracy as ma
import dataSetSplit as sp
import pickle
import os
import copy
import zlib
import numpy as np
import io

model1 = mg.create_model()
model1.load_weights('backup/model_weights.h5')
# Make a copy of the weights
model1_weights = copy.deepcopy(model1.get_weights())

# Quantize the weights to 8-bit integers
quantized_weights = [np.round(w * 127.5 / np.max(np.abs(w))).astype(np.int8) for w in model1_weights]

buf = io.BytesIO()
np.savez(buf, *quantized_weights)
model_bytes = buf.getvalue()

compressed_model = zlib.compress(model_bytes)

my_string_quantized = base64.b64encode(compressed_model).decode('utf-8')

print("Size of encoded quantized model parameter is (String Data type): {:.2f} MB".format(len(my_string_quantized) / (1024 * 1024)))
print(type(my_string_quantized))
