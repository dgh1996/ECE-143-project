import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
import matplotlib.pyplot as plt

data = pd.read_csv(r"C://Users//shion//Desktop//ECE_143//prjct//weatherAUS.csv")

print(data.shape)  
data.dropna(subset=['Location', 'Date'], inplace = True)
data = data[['Location', 'Date', 'RainToday', 'RISK_MM']]
data = data.loc[data['RainToday'] == "Yes"]

print(data.shape)
print(data.Location.unique())

States = ["VIC", "NSW", "SA", "QLD", "WA", "TAS", "NT"]


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

StatesDic = {"VIC":VIC, "NSW":NSW, "SA":SA, "QLD":QLD, "WA":WA, "TAS":TAS, "NT":NT}


years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
LocationStats = {}
for location in Locations:
    tmpData = data.loc[data['Location'] == location]
   # print(tmpData.iloc[0]['Date'] )
    stat = [len(tmpData.loc[tmpData['Date'].str.startswith(str(year))]) for year in years]
    LocationStats[location] = stat 

#print(str(LocationStats))

# for i in range(len(Locations)):
#     location = Locations[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats')
# plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol = 2)



StatesStats = {} #stateName: 8 years of ave days of raining

for state in States:
    LocList = StatesDic[state]
    plotDic = [0,0,0,0,0,0,0,0] #year
    for i in range(len(LocList)):
        for year in range(len(LocationStats[LocList[i]])):
            plotDic[year] += LocationStats[LocList[i]][year]
    for idx in range(len(plotDic)):
        plotDic[idx] = plotDic[idx] / len(LocList)
    StatesStats[state] = plotDic

for key in StatesStats:
    print(str(StatesStats[key]))
        # location = Locations[i]
        # plt.plot(years, LocationStats[location], label=location.format(i=i))
    


for i in range(len(States)):
    state = States[i]
    plt.plot(years, StatesStats[state], label=state.format(i=i))

plt.xlabel('Years')
plt.ylabel('Number of Raining Days')
plt.title('Raining Statistics with Years in All States in Australia')
plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))

# for i in range(len(NSW)):
#     location = NSW[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in NSW')
# plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))




# for i in range(len(VIC)):
#     location = VIC[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in VIC')
# plt.legend(loc='best')




# for i in range(len(SA)):
#     location = SA[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in SA')
# plt.legend(loc='best')



# for i in range(len(QLD)):
#     location = QLD[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in QLD')
# plt.legend(loc='best')



# for i in range(len(WA)):
#     location = WA[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in WA')
# plt.legend(loc='best')




# for i in range(len(TAS)):
#     location = TAS[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in TAS')
# plt.legend(loc='best')




# for i in range(len(NT)):
#     location = NT[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in NT')
# plt.legend(loc='best')



# for i in range(len(QLD)):
#     location = QLD[i]
#     plt.plot(years, LocationStats[location], label=location.format(i=i))

# plt.xlabel('Years')
# plt.ylabel('Number of Raining Days')
# plt.title('Australian Raining Stats in QLD')
# plt.legend(loc='best')

plt.show()
