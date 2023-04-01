#project initilaization
#libraries
from sklearn.model_selection import train_test_split
import pandas as pd
#files
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp
import modelAggregation 
import fileHandle as fh
import csv
import numpy as np
import saveModelData as sm

#cart initialisation remove files that have alredy having
def resetProject():
    fh.resetModelData()


#remove stored data in carData file
def recodeDataRemove():
    
    with open('dataset/cartData.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        rows = [row for row in reader]

    with open('dataset/cartData.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows[0:1])
        writer.writerows(rows[4:])

    print("Removes training data")
    


#Globle aggregation process
def globleAggregationProcess():
          print("Strat local training ------->")
          model=mg.create_model()
          model.load_weights('modelData/model_weights.h5')
          #traing model using cartdata
          print("Split dataset")
          x_train,y_train = sp.splitCartData()
          mt.continuoustrainModel(model,x_train,y_train)
          #test model using local data
          x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
          ma.getModelAccuracy(model,x_test_np,y_test_np)
          #adding differential privacy
          differentialPrivacy()
          #clear the csv file
          recodeDataRemove()
          #aggregate the models
          modelAggregation.modelAggregation()
          #remove received files
          fh.removeFiles()
          return "Aggregated"

#initial aggregation process  
def initialAggregationProcess():
     modelAggregation.initialModelAggregation()
     fh.removeFiles()


def differentialPrivacy():
    print("Starting adding differential privacy ------->")
    model=mg.create_model()
    model.load_weights('modelData/model_weights.h5')
    #traing model using cartdata
    print("Split dataset")
    #test model using local data
    print("Get Local model accuracy----->")
    x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
    localModelAccuracy =  ma.getModelAccuracy(model,x_test_np,y_test_np)
    
    def loopProcess():
        # Define the standard deviation of the noise
        std_dev = 0.01
        stopRange =5
        # Get the model weights
        model_weights = model.get_weights()
        tempModel=mg.create_model()

        print("Add differntial privacy----->")
        # Add Gaussian noise to the model weights
        for i in range(len(model_weights)):
            model_weights[i] += np.random.normal(loc=0.0, scale=std_dev, size=model_weights[i].shape)

        # Set the modified weights back to the model
        tempModel.set_weights(model_weights)
        print("Differential privacy model accuracy----->")
        differentialPrivacyModelAccuracy = ma.getModelAccuracy(tempModel,x_test_np,y_test_np)
        if( differentialPrivacyModelAccuracy > localModelAccuracy - stopRange ) and (differentialPrivacyModelAccuracy < localModelAccuracy + stopRange) :
            print(localModelAccuracy)
            print(differentialPrivacyModelAccuracy)
            
            print("Stop loop process")
            sm.saveModelData(tempModel)
            return True
        
        else:
            return False
        
    x=0
    while True:
       print("Iteration No : ",x)
       returnVal= loopProcess()
       if returnVal == True:
           break
      
       x=x+1

