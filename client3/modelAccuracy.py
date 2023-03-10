#get model accuracy

#libraries
from sklearn.metrics import accuracy_score

def getModelAccuracy(model,test_data1,test_labels1):
      #Predict model 1  test using test date
    y_pred_model_1 = model.predict(test_data1)

    # The predictions are in the form of probability of each class, so we will take the class with highest probability
    y_pred_model_1 = y_pred_model_1.argmax(axis=-1)

    # Calculate the accuracy of the model
    
    accuracy_model_1 = accuracy_score(test_labels1, y_pred_model_1)
    print("Model  Accuracy:", accuracy_model_1*100)
    return accuracy_model_1