import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def correlation(data):
	'''Plot the correlation chart for the given data
	Parameter:
	data - Input dataframe
	'''
	#Clean the data
	datac = data.copy(deep=True)
	datac['RainToday'].replace({'No':0,'Yes':1},inplace = True)
	datac['RainTomorrow'].replace({'No':0,'Yes':1},inplace = True)
	data1 = data[['RainToday', 'RainTomorrow']]
	data1 = data1.dropna(inplace = False)
	#Extract usable features
	data2 = data[['MinTemp','MaxTemp', 'WindSpeed9am','WindSpeed3pm','Humidity9am', 'Humidity3pm', 'Cloud9am', 'Cloud3pm', 'Pressure9am', 'Pressure3pm','RainToday', 'RainTomorrow'] ]
	#Find the correlations
	corr = data2.corr()
	#Plot the correlations as a heatmap
	plt.figure(2) 
	ax = sns.heatmap(corr, annot = True, annot_kws = {'size':6, 'weight': 'bold'})
	ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)
	ax.set_title('correlation table')
	ax.tick_params(labelsize = 7)
	plt.tight_layout()
	plt.savefig('corr.png',dpi=300,bbox_inches = 'tight')
	plt.show()

