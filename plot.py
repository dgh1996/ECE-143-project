import matplotlib.pyplot as plt
import numpy as np
def countseq(l):
	'''Simple helper function to count sequences
	Parameter:
	l - A list
	Return:
	maxc - Longest number of sequences of 0
	'''
	maxc=0
	count=0
	for i in l:
	    if i==0:
	        count+=1
	        maxc=max(maxc,count)
	    else:
	        count=0
	return maxc

def yearplots(data):
	'''Plot the yearly data comparisons of the three selected cities
	Parameter:
	data - Input dataframe
	'''
	#Separate and clean the data
	years=list(range(2009,2017))
	data_sl=data.loc[data["Location"]=="Sale"]
	data_pl=data.loc[data["Location"]=="Portland"]
	data_bc=data.loc[data["Location"]=="BadgerysCreek"]
	data_sl_y=[]
	data_pl_y=[]
	data_bc_y=[]
	rt_sl_i=[]
	rt_pl_i=[]
	rt_bc_i=[]
	mt_sl_i=[]
	mt_pl_i=[]
	mt_bc_i=[]
	for i in years:
	    data_sl_y.append(data_sl[data_sl["Date"].str.contains(str(i),na=False)])
	    data_pl_y.append(data_pl[data_pl["Date"].str.contains(str(i),na=False)])
	    data_bc_y.append(data_bc[data_bc["Date"].str.contains(str(i),na=False)])
	for i in range(len(years)):
	    rt_sl_i.append([1 if i=="Yes" else 0 for i in data_sl_y[i]["RainToday"]])
	    rt_pl_i.append([1 if i=="Yes" else 0 for i in data_pl_y[i]["RainToday"]])
	    rt_bc_i.append([1 if i=="Yes" else 0 for i in data_bc_y[i]["RainToday"]])
	    mt_sl_i.append(data_sl_y[i]["MaxTemp"])
	    mt_pl_i.append(data_pl_y[i]["MaxTemp"])
	    mt_bc_i.append(data_bc_y[i]["MaxTemp"])
	    
	#Extract the data for plotting
	rt_sl=[sum(i) for i in rt_sl_i]
	dd_sl=[countseq(i) for i in rt_sl_i]
	rt_pl=[sum(i) for i in rt_pl_i]
	dd_pl=[countseq(i) for i in rt_pl_i]
	rt_bc=[sum(i) for i in rt_bc_i]
	dd_bc=[countseq(i) for i in rt_bc_i]
	#Arrange the side-by-side bar plots
	index=np.arange(len(rt_sl))
	bw=0.2
	#Plot the rainy days chart
	b_sl=plt.bar(index-bw,rt_pl,bw,label="Portland",color="#ff7f0e")
	b_s2=plt.bar(index,rt_sl,bw,label="Sale",color="#1f77b4")
	b_s3=plt.bar(index+bw,rt_bc,bw,label="BadgerysCreek",color="#2ca02c")
	plt.xticks(index,years)
	plt.legend(bbox_to_anchor=[1,1.03])
	plt.xlabel("Year")
	plt.ylabel("Number of rainy days in year (day)")
	plt.title("Comparison of Number of Rainy Days by Year(2009-2016)")
	plt.savefig("RainyDays.png",dpi=800,bbox_inches="tight")
	plt.show()
	#Plot the dry streak chart
	b_sl=plt.bar(index-bw,dd_pl,bw,label="Portland",color="#ff7f0e")
	b_s2=plt.bar(index,dd_sl,bw,label="Sale",color="#1f77b4")
	b_s3=plt.bar(index+bw,dd_bc,bw,label="BadgerysCreek",color="#2ca02c")
	plt.xticks(index,years)
	plt.legend(bbox_to_anchor=[1,1.03])
	plt.xlabel("Year")
	plt.ylabel("Longest dry streak in year (day)")
	plt.title("Comparison of Longest Dry Streak by Year(2009-2016)")
	plt.savefig("DryStreak.png",dpi=800,bbox_inches="tight")
	plt.show()

def seasonplot(data):
	'''Plot the seasonal comparison data for the three selected cities
	Parameter:
	data - Input dataframe
	'''
	data_sl=data.loc[data["Location"]=="Sale"]
	data_pl=data.loc[data["Location"]=="Portland"]
	data_bc=data.loc[data["Location"]=="BadgerysCreek"]
	#Construct all days of each season to extract from dataframe
	seasons=[["12-","1-","2-"],["3-","4-","5-"],["6-","7-","8-"],["9-","10-","11-"]]
	extended_seasons=[[],[],[],[]]
	for i in range(len(seasons)):
	    for j in seasons[i]:
	        for k in range(1,32):
	            if k<10:
	                extended_seasons[i].append(j+"0"+str(k))
	            else:
	                extended_seasons[i].append(j+str(k))
	#Extract and clean the data
	data_sl_s=[]
	data_pl_s=[]
	data_bc_s=[]
	rt_sl_s=[]
	rt_pl_s=[]
	rt_bc_s=[]
	for i in range(len(seasons)):
	    data_sl_s.append(data_sl[data_sl["Date"].str.endswith(tuple(extended_seasons[i]))])
	    data_pl_s.append(data_pl[data_pl["Date"].str.endswith(tuple(extended_seasons[i]))])
	    data_bc_s.append(data_bc[data_bc["Date"].str.endswith(tuple(extended_seasons[i]))])
	for i in range(len(seasons)):
	    rt_sl_s.append([1 if i=="Yes" else 0 for i in data_sl_s[i]["RainToday"]])
	    rt_pl_s.append([1 if i=="Yes" else 0 for i in data_pl_s[i]["RainToday"]])
	    rt_bc_s.append([1 if i=="Yes" else 0 for i in data_bc_s[i]["RainToday"]])
	rt_sl=[sum(i) for i in rt_sl_s]
	rt_pl=[sum(i) for i in rt_pl_s]
	rt_bc=[sum(i) for i in rt_bc_s]
	#Arrange the side-by-side bar plots
	index=np.arange(len(rt_sl))
	bw=0.2
	#Plot the seasonal rainy day data
	b_sl=plt.bar(index-bw,rt_pl,bw,label="Portland",color="#ff7f0e")
	b_s2=plt.bar(index,rt_sl,bw,label="Sale",color="#1f77b4")
	b_s3=plt.bar(index+bw,rt_bc,bw,label="BadgerysCreek",color="#2ca02c")
	plt.xticks(index,["Summer","Fall","Winter","Spring"])
	plt.legend(bbox_to_anchor=[1.37,1.03])
	plt.xlabel("Season")
	plt.ylabel("Total rainy days in season (day)")
	plt.title("Comparison of Number of Rainy Days by Season (2009-2016)")
	plt.savefig("RainyDaysSeason.png",dpi=800,bbox_inches="tight")
	plt.show()