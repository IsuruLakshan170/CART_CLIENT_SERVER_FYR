#project initilaization
#libraries
from sklearn.model_selection import train_test_split
import pandas as pd
#files
import initModel as im
import modelGenerator as mg
import modelTraining as mt
import modelAccuracy as ma
import dataSetSplit as sp
import modelAggregation 
import fileHandle as fh
import client

#cart initialisation 
def initProject():
    im.intModel()

#inserted data analysis
def datasetAnalize():
      cartData = pd.read_csv('dataset/cartData.csv')
      if(len(cartData) == 3):
          print("Strat local training ------->")
          model=mg.create_model()
          model.load_weights('modelData/model_weights.h5')
          #traing model using cartdata
          x_train,y_train = sp.splitCartData()
          mt.continuoustrainModel(model,x_train,y_train)
          #test model using local data
          x_train_np, y_train_np,x_test_np,y_test_np =sp.splitDataset()
          ma.getModelAccuracy(model,x_test_np,y_test_np)
          #clear the csv file
          recodeDataRemove()
          #aggregate the models
          client.clientConnect()
          modelAggregation.modelAggregation()
          #remove received files
          fh.removeFiles()
          return "Aggregated"
      return ""
  

#remove stored data in carData file
def recodeDataRemove():
    import csv

    with open('dataset/cartData.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        rows = [row for row in reader]

    with open('dataset/cartData.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows[0:1])
        writer.writerows(rows[4:])

    print("Removes training data")
    


