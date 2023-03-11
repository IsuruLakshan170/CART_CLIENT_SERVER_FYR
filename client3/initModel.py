#initialization of ML mode , taing , test and save
import dataSetGenerator as ds
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp
import modelAggregation 
import fileHandle as fh
import c3


def intModel():
    # # #generate dataset
    # ds.DatasetGenerator(10000)
    # # split data and use for predict accuracy
    # x_train,y_train,x_test,y_test =sp.splitDataset()
    # mt.trainModel(model,x_train,y_train)
    c3.clientConnect()
    modelAggregation.initialModelAggregation()
    fh.removeInitFiles()
    # return model
    
