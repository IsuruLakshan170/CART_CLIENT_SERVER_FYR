#model Aggregations
import modelGenerator as mg
import numpy as np
import modelAccuracy as ma
import dataSetSplit as sp
import saveModelData  as sm
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)
import dataSetGenerator as dg

# model aggregation when cart training after 
def modelAggregation():
    print("Strat aggregation")
    parameterArray = [0] * 3
    model=mg.create_model()
    # dg.DatasetGenerator(10000)

    # x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
    for i in range(2):
        num=i+1
        print("Received Model ------> ",num)
        model.load_weights(f'receivedModelParameter/model_weights_{num}.h5')
       
        # ma.getModelAccuracy(model,x_test_np,y_test_np)
        receivedModelParameters  = model.get_weights()

        parameterArray[i]=receivedModelParameters
    print("Local Model ------> ")
    model.load_weights('modelData/model_weights.h5')
    # ma.getModelAccuracy(model,x_test_np,y_test_np)
    receivedModelParameters  = model.get_weights()
   
    parameterArray[2]=receivedModelParameters
    averageWeight=[(w1 + w2 + w3 )/3 for w1, w2 , w3 in zip(parameterArray[0], parameterArray[1],parameterArray[2])]
    modelAG=mg.create_model()
    modelAG.set_weights(averageWeight)
    print("Aggregrated model ------> ")
 
    # ma.getModelAccuracy(modelAG,x_test_np,y_test_np)
    #save averaged parameters
    sm.saveModelData(model)
    print("Aggregrate Complete")
    
# initial model aggregations
def initialModelAggregation():
    print("Strat initial aggregation")
    # x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
    model1 =mg.create_model()
    model1.load_weights(f'receivedModelParameter/model_weights_1.h5')
    print("Received model 1 accuracy ")
    # ma.getModelAccuracy(model1,x_test_np,y_test_np)
    weight_1  = model1.get_weights()

    model2=mg.create_model()
    model2.load_weights(f'receivedModelParameter/model_weights_2.h5')
    print("Received model 2 accuracy ")
    # ma.getModelAccuracy(model2,x_test_np,y_test_np)
    weight_2  = model2.get_weights()
    
    
    averageWeight=[(w1 + w2 )/2 for w1, w2 in zip(weight_1, weight_2 )]

    modelAG=mg.create_model()
    modelAG.set_weights(averageWeight)
    print("Aggregated Model ------> ")
    # ma.getModelAccuracy(modelAG,x_test_np,y_test_np)
    #save averaged parameters
    sm.saveModelData(modelAG)

    print("Aggregrate Complete")
    
