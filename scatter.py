import numpy as np
import pandas as pd
import math
import random
import matplotlib.pyplot as plt
def scatter(model,cleanx,cleany):
	''' Plot the scatter plots of the sample datapoints for the given model
	Parameters:
	model - The model used
	cleanx - The cleaned x data 
	cleany - The cleaned y data
	'''
	countr=0
	countn=0
	limit=50
	X_r=[]
	Y_r=[]
	cxr=[]
	X_n=[]
	Y_n=[]
	cxn=[]
	#Search for 50 of each type of data
	for i in range(2000):
	    if(cleany[i]==1):
	        countr+=1
	        if(countr<=limit):
	            X_r.append(cleanx[i][71])
	            Y_r.append(cleanx[i][76])
	            cxr.append(cleanx[i])
	    else:
	        countn+=1
	        if(countn<=limit):
	            X_n.append(cleanx[i][71])
	            Y_n.append(cleanx[i][76])
	            cxn.append(cleanx[i])
	    if(countr>=limit and countn>=limit):
	        break
	#Plot the scatters of the original data
	plt.title("Spread of first 50 datapoints")
	plt.scatter(X_r,Y_r,label="Rain",color="blue")
	plt.scatter(X_n,Y_n,label="NoRain",color="#999900")
	plt.xlabel("Temperature(°C)")
	plt.ylabel("Humidity(%)")
	plt.legend(bbox_to_anchor=[1,1.05])
	plt.savefig("Sample.png",dpi=800,bbox_inches="tight")
	plt.show()
	#Use the model to calculate the prediction spread
	predyr=model.predict(cxr)
	predyn=model.predict(cxn)
	X_rr=[]
	X_f=[]
	X_nn=[]
	Y_rr=[]
	Y_f=[]
	Y_nn=[]
	for i in range(limit):
	    if(predyr[i]==1):
	        X_rr.append(X_r[i])
	        Y_rr.append(Y_r[i])
	    else:
	        X_f.append(X_r[i])
	        Y_f.append(Y_r[i])
	    if(predyn[i]==1):
	        X_f.append(X_n[i])
	        Y_f.append(Y_n[i])
	    else:
	        X_nn.append(X_n[i])
	        Y_nn.append(Y_n[i])
	#Plot the predicted scatter instead
	plt.scatter(X_rr,Y_rr,label="Predicted Rain",color="blue")
	plt.scatter(X_f,Y_f,label="Incorrect prediction",color="red")
	plt.scatter(X_nn,Y_nn,label="Predicted no rain",color="#999900")
	plt.title("Spread and prediction of first 50 datapoints")
	plt.xlabel("Temperature(°C)")
	plt.ylabel("Humidity(%)")
	plt.legend(bbox_to_anchor=[1,1.05])
	plt.savefig("SamplePred.png",dpi=800,bbox_inches="tight")
	plt.show()

