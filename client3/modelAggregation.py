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
    parameterArray = [0] * 6
    model=mg.create_model()
    # dg.DatasetGenerator(10000)

    x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
    for i in range(5):
        num=i+1
        print("Received Model ------> ",num)
        model.load_weights(f'receivedModelParameter/model_weights_{num}.h5')
       
        ma.getModelAccuracy(model,x_test_np,y_test_np)
        receivedModelParameters  = model.get_weights()
        print(type(receivedModelParameters))
        parameterArray[i]=receivedModelParameters
    print("Local Model ------> ")
    model.load_weights('modelData/model_weights.h5')
    ma.getModelAccuracy(model,x_test_np,y_test_np)
    receivedModelParameters  = model.get_weights()
    print(type(receivedModelParameters))
    parameterArray[5]=receivedModelParameters
    # averageWeight=[(w1 + w2 + w3 + w4 + w5 + w6 )/6 for w1, w2, w3, w4, w5, w6 in zip(parameterArray[0], parameterArray[1], parameterArray[2], parameterArray[3], parameterArray[4], parameterArray[5])]
    averageWeight=[(w1 + w2 + w3+ w4 + w5 + w6 )/6 for w1, w2 , w3, w4 , w5 , w6 in zip(parameterArray[0], parameterArray[1],parameterArray[2], parameterArray[3],parameterArray[4], parameterArray[1])]
    modelAG=mg.create_model()
    modelAG.set_weights(averageWeight)
    print("Aggregrated model ------> ")
 
    ma.getModelAccuracy(modelAG,x_test_np,y_test_np)
    #save averaged parameters
    sm.saveModelData(model)
    print("Aggregrate Complete")
    
# initial model aggregations
def initialModelAggregation():
    print("Strat initial aggregation")
    x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
    model1 =mg.create_model()
    model1.load_weights(f'initModelParameters/model_weights_1.h5')
    ma.getModelAccuracy(model1,x_test_np,y_test_np)
    weight_1  = model1.get_weights()

    model2=mg.create_model()
    model2.load_weights(f'initModelParameters/model_weights_2.h5')
    ma.getModelAccuracy(model2,x_test_np,y_test_np)
    weight_2  = model2.get_weights()
    
    model3=mg.create_model()
    model3.load_weights(f'initModelParameters/model_weights_3.h5')
    ma.getModelAccuracy(model3,x_test_np,y_test_np)
    weight_3  = model3.get_weights()
    
    model4=mg.create_model()
    model4.load_weights(f'initModelParameters/model_weights_4.h5')
    ma.getModelAccuracy(model4,x_test_np,y_test_np)
    weight_4  = model4.get_weights()
    
    model5=mg.create_model()
    model5.load_weights(f'initModelParameters/model_weights_5.h5')
    ma.getModelAccuracy(model5,x_test_np,y_test_np)
    weight_5 = model5.get_weights()
    
    averageWeight=[(w1 + w2 + w3+ w4 + w5 )/5 for w1, w2 , w3, w4 , w5 in zip(weight_1, weight_2 ,weight_3, weight_4,weight_5)]
    # averageWeight=[(w1 + w2 + w3  )/3 for w1, w2 ,w3 in zip(weight_4, weight_2, weight_3)]

    modelAG=mg.create_model()
    modelAG.set_weights(averageWeight)
    print("Aggregated Model ------> ")
    ma.getModelAccuracy(modelAG,x_test_np,y_test_np)
    #save averaged parameters
    sm.saveModelData(modelAG)

    print("Aggregrate Complete")
    

# def initialModelAggregation():
#     print("Strat initial aggregation")
#     parameterArray = [0] * 6
#     model=mg.create_model()
#     # dg.DatasetGenerator(10000)

#     x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
#     for i in range(5):
#         num=i+1
#         print("Received Model ------> ",num)
#         model.load_weights(f'initModelParameters/model_weights_{num}.h5')
#         ma.getModelAccuracy(model,x_test_np,y_test_np)
#         receivedModelParameters  = model.get_weights()
#         parameterArray[i]=receivedModelParameters

#     # averageWeight=[(w1 + w2 + w3 + w4 + w5 + w6 )/6 for w1, w2, w3, w4, w5, w6 in zip(parameterArray[0], parameterArray[1], parameterArray[2], parameterArray[3], parameterArray[4], parameterArray[5])]
#     averageWeight=[(w1 + w2 + w3+ w4 + w5 )/5 for w1, w2 , w3, w4 , w5 in zip(parameterArray[0], parameterArray[1],parameterArray[2], parameterArray[3],parameterArray[4])]
#     model.set_weights(averageWeight)
#     print("Aggregated Model ------> ",num)
#     ma.getModelAccuracy(model,x_test_np,y_test_np)
#      #save averaged parameters
#     saveModel.saveModelData(model)
#     print("Aggregrate Complete")



