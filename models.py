import numpy as np
import pandas as pd
import math
import random
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

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
    cleanf - The feature titles of the columns
    '''
    #Use one-hot encoding for features such as location
    onehotl=[]
    for onehot in onehots:
        onehotl.append(pd.get_dummies(data[onehot],prefix=onehot,drop_first=True))
    cleanx=pd.concat(onehotl,axis=1).join(data[features])
    #For features that may contain NA values, fill them with average in the category
    for feature in features:
        cleanx[feature].fillna(cleanx[feature].mean(),inplace=True)
    cleanf=cleanx.columns
    cleanx=cleanx.values
    #Encode the value section
    cleany=[0 if i=="No" else 1 for i in data["RainTomorrow"].values]
    return cleanx, cleany, cleanf

def trainModel(cleanx,cleany):
    '''Trains four different models and compare their performances. Notice that these are very primitive models
    that can be improved and also can vary a lot every time the function is run
    Parameters:
    cleanx - Expects a cleaned sample data
    cleany - Expects a cleaned value data
    
    Returns:
    model - The selected model
    '''
    models={}
    #Logistics Regression Model
    trainx,trainy,valx,valy,testx,testy = data_split(cleanx,cleany)
    lrmodel=LogisticRegression(solver="lbfgs",max_iter=1000)
    lrmodel.fit(trainx,trainy)
    models["Logistic"]=lrmodel.score(valx,valy)
    #Linear Regression Model
    llmodel=LinearRegression()
    llmodel.fit(trainx,trainy)
    predy=llmodel.predict(valx)
    #Class prediction code for linear regression
    correct=0
    for i in range(len(valy)):
        if (predy[i]>0.5 and valy[i]==1) or (predy[i]<0.5 and valy[i]==0):
            correct+=1
    models["Linear"]=correct/len(valy)
    #Support Vector Machine
    svmodel=LinearSVC(max_iter=1000)
    svmodel.fit(trainx,trainy)
    models["SVM"]=svmodel.score(valx,valy)
    #K Nearest Neighbours Model
    knmodel=KNeighborsClassifier()
    knmodel.fit(trainx,trainy)
    models["KNN"]=knmodel.score(valx,valy)
    print(models)
    models=[(k,v) for k,v in models.items()]
    models=sorted(models,key=lambda x:x[1])
    x=[x[0] for x in models]
    label=[x[1] for x in models]
    plt.bar(x,label)
    plt.title("Accuracy of different models over the validation set")
    plt.xlabel("Models")
    plt.ylabel("Validation set accuracy")
    plt.ylim(0.5,1.0)
    plt.savefig("Accuracy.png",dpi=800,bbox_inches="tight")
    plt.show()
    return lrmodel