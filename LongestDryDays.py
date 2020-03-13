import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
import matplotlib.pyplot as plt

data = pd.read_csv(r"C://Users//shion//Desktop//ECE_143//prjct//weatherAUS.csv")

print(data.shape)  
data.dropna(subset=['Location', 'Date'], inplace = True)
data = data[['Location', 'Date', 'Rainfall']]
print(data[0:100])



WeUse = ['Sale', 'Portland', 'BadgerysCreek']
WeUseDic = {}
for Loc in WeUse:
    tmpData = data.loc[data['Location'] == Loc]
    
    RainFall = tmpData[['Rainfall']]
    WeUseDic[Loc] = RainFall['Rainfall'].to_list()
    print(max(WeUseDic[Loc]))

data = [WeUseDic[key] for key in WeUseDic]
for i in range(len(data)):
    data[i] = [i for i in data[i] if i < 20 and i > 0]

plt.hist(data, bins=25, label=WeUse)
plt.title("The amount of rainfall")
plt.xlabel("rainfall(milimeters)")
plt.ylabel("Days")
plt.legend(loc='best')
plt.show()