import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv(r"C://Users//shion//Desktop//ECE_143//prjct//weatherAUS.csv")

print(data.shape)  
data.dropna(subset=['Location', 'Date'], inplace = True)
data = data[['Location', 'Date', 'RainToday']]
data = data.loc[data['RainToday'] == "Yes"]
data["month"]= pd.DatetimeIndex(data['Date']).month

def label_season (row):
    if row['month'] in [2,3,4] :
      return 'Spring'
    if row['month'] in [5,6,7] :
      return 'Summer'
    if row['month'] in [8,9,10] :
      return 'Fall'
    if row['month'] in [11,12,1] :
      return 'Winter'
    return 'Other'

data['Season'] = data.apply(lambda row: label_season(row), axis=1)




print("Data from Katherine, Uluru, Nhil and Melbourne are incomplete so they won't be considered")
Locations = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree', 'Newcastle',
 'NorahHead', 'NorfolkIsland', 'Penrith', 'Richmond', 'Sydney', 'SydneyAirport',
 'WaggaWagga', 'Williamtown', 'Wollongong', 'Canberra', 'Tuggeranong',
 'MountGinini', 'Ballarat', 'Bendigo', 'Sale', 'MelbourneAirport',
 'Mildura', 'Portland', 'Watsonia', 'Dartmoor', 'Brisbane', 'Cairns',
 'GoldCoast', 'Townsville', 'Adelaide', 'MountGambier', 'Nuriootpa', 'Woomera',
 'Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport', 'Perth', 'SalmonGums',
 'Walpole', 'Hobart', 'Launceston', 'AliceSprings', 'Darwin']


VIC = ['Ballarat', 'Bendigo', 'Sale', 'MelbourneAirport', 'Mildura', 'Portland', 'Watsonia', 'Dartmoor']
NSW = ['Albury', 'BadgerysCreek', 'Cobar', 'CoffsHarbour', 'Moree', 'Newcastle', 'NorahHead', 'Penrith', 'Richmond', 'Sydney', 
'SydneyAirport', 'WaggaWagga', 'Williamtown', 'Canberra', 'Tuggeranong', 'MountGinini', 'NorfolkIsland']
SA = ['Wollongong', 'Adelaide', 'MountGambier', 'Nuriootpa', 'Woomera']
QLD = ['Brisbane', 'Cairns', 'GoldCoast', 'Townsville', ]
WA = ['Albany', 'Witchcliffe', 'PearceRAAF', 'PerthAirport', 'Perth', 'SalmonGums', 'Walpole']
TAS = ['Hobart', 'Launceston']
NT = ['AliceSprings', 'Darwin']

States = ["VIC", "NSW", "SA", "QLD", "WA", "TAS", "NT"]
StatesDic = {"VIC":VIC, "NSW":NSW, "SA":SA, "QLD":QLD, "WA":WA, "TAS":TAS, "NT":NT}

Season = ["Spring", "Summer", "Fall", "Winter"]
mToS = {1:"Winter", 2:"Spring", 3:"Spring", 4:"Spring", 5:"Summer", 6:"Summer", 7:"Summer", 8:"Fall", 9:"Fall", 10:"Fall", 11:"Winter", 12:"Winter"}
years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
SeasonStats = {}# loc:[[spring of several years], summer..., fall..., winter...]


for location in Locations:
    tmpData = data.loc[data['Location'] == location]
    spring = [len(tmpData.loc[(tmpData['Season'] == 'Spring') & (tmpData['Date'].str.startswith(str(year)))]) for year in years]
    summer = [len(tmpData.loc[(tmpData['Season'] == 'Summer') & (tmpData['Date'].str.startswith(str(year)))]) for year in years]
    fall = [len(tmpData.loc[(tmpData['Season'] == 'Fall') & (tmpData['Date'].str.startswith(str(year)))]) for year in years]
    winter = [len(tmpData.loc[(tmpData['Season'] == 'Winter') & (tmpData['Date'].str.startswith(str(year)))]) for year in years]
    SeasonStats[location] = [spring, summer, fall, winter]

def ave(lst): 
    return sum(lst) / len(lst) 

def AVGofStates(lstofLoc):
    sp = []
    sm = []
    fa = []
    wt = []
    for loc in lstofLoc:
        # for lst in SeasonStats[loc]:
        sp = sp + SeasonStats[loc][0]
        sm = sm + SeasonStats[loc][1]
        fa = fa + SeasonStats[loc][2]
        wt = wt + SeasonStats[loc][3]
    return [ave(sp), ave(sm), ave(fa), ave(wt)]

statesStats = {} # state:[spring, summer, fall, winter]
for state in States:
    ListofLoc = StatesDic[state]
    statesStats[state] = AVGofStates(ListofLoc)

#print(str(statesStats))

for i in range(len(States)):
    state = States[i]
    plt.plot(Season, statesStats[state], label=state.format(i=i))

plt.xlabel('Seasons')
plt.ylabel('Average of raining days in 3 months')
plt.title('Australian Raining Stats of four periods')
plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol = 1)


plt.show()
