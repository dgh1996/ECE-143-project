import numpy as np
import pandas as pd
import math
import random
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression, LinearRegression
def data_split(sample,value):
    '''Construct train-val-test split from raw data
    Parameters:
    sample - Raw sample data
    value - Raw value data
    
    Return:
    trainx, valx, testx - Splitted data of samples
    trainy, valy, testy - Splitted data of values
    '''
    #Shuffles the data randomly while maintaining index correspondence
    sample,value=shuffle(sample,value)
    size=len(sample)
    #Use a roughly 80-10-10 split of train-val-test
    train_size=math.floor(size*0.8)
    val_size=math.floor(size*0.9)
    return sample[:train_size],value[:train_size],sample[train_size+1:val_size],value[train_size+1:val_size],sample[val_size+1:],value[val_size+1:]

def learningProcessor(data,features,onehots):
    '''Process the data to enable one-hot encoding and replace unknown values with average values in that category.
    Parameter:
    data - The dataframe that contains the information
    features - The features to be considered in the training data
    onehots - The features needs to be reconsidered for one-hot encoding
    
    Return:
    cleanx - Cleaned samples
    cleany - Cleaned values
    '''
    #Use one-hot encoding for features such as location
    onehotl=[]
    for onehot in onehots:
        onehotl.append(pd.get_dummies(data[onehot],prefix=onehot,drop_first=True))
    cleanx=pd.concat(onehotl,axis=1).join(data[features])
    #For features that may contain NA values, fill them with average in the category
    for feature in features:
        cleanx[feature].fillna(cleanx[feature].mean(),inplace=True)
    cleanx=cleanx.values
    #Encode the value section
    cleany=[0 if i=="No" else 1 for i in data["RainTomorrow"].values]
    return cleanx, cleany

def trainModel(cleanx,cleany):
    '''Trains the model
    Parameters:
    cleanx - Expects a cleaned sample data
    cleany - Expects a cleaned value data
    
    Returns:
    model - The selected model
    '''
    trainx,trainy,valx,valy,testx,testy = data_split(cleanx,cleany)
    lrmodel=LogisticRegression(solver="lbfgs",max_iter=2000)
    lrmodel.fit(trainx,trainy)
    print("Validation set performance: %f"%lrmodel.score(valx,valy))
    print("Test set accuracy: %f"%lrmodel.score(testx,testy))
    data=pd.read_csv("weatherAUS.csv")

onehots=["Location","WindGustDir"]
features=["MinTemp","MaxTemp","Rainfall","WindGustSpeed","Humidity9am","Humidity3pm","Pressure9am","Pressure3pm","Temp9am","Temp3pm"]
cleanx,cleany = learningProcessor(data,features,onehots)
trainModel(cleanx,cleany)
