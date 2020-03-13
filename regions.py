import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def regionalize(data):
	'''Map the cities in the data to different regions.
	Parameter:
	data - Input dataframe
	Returns:
	data - Modified data
	'''
	str_sa="South Australia"
	str_wa="Western Australia"
	str_nsw="New South Wales"
	str_nt="Northern Territory"
	str_vt="Victoria"
	str_ql="Queensland"
	str_act="Australian Capital Territory"
	str_tm="Tasmania"
	str_et="External Territory"
	mapregion={0:str_sa,1:str_wa,2:str_nsw,3:str_nt,4:str_nsw,5:str_vt,6:str_vt,7:str_ql,8:str_ql,\
	           9:str_act,10:str_nsw,11:str_nsw,12:str_vt,13:str_nt,14:str_ql,15:str_tm,16:str_nt,\
	           17:str_tm,18:str_vt,19:str_vt,20:str_vt,21:str_nsw,22:str_sa,23:str_nsw,24:str_nsw,\
	           25:str_vt,26:str_nsw,27:str_et,28:str_sa,29:str_wa,30:str_nsw,31:str_wa,32:str_wa,\
	           33:str_vt,34:str_nsw,35:str_vt,36:str_wa,37:str_nsw,38:str_nsw,39:str_ql,40:str_act,\
	           41:str_nt,42:str_nsw,43:str_wa,44:str_vt,45:str_nsw,46:str_wa,47:str_nsw,48:str_sa}
	locset = list(set(data["Location"]))
	for i in range(len(locset)):
	    mapregion[locset[i]]=mapregion[i]
	data["Region"]=[mapregion[i] for i in data["Location"]]
	return data

def regionplot(data,str_reg):
	'''Do some simple plotting of a certain regions
	Parameters:
	data - Input dataframe
	str_reg - The string representation for the region
	'''
	assert isinstance(str_reg,str),"Second input must be a string"
	#Extract the region data
	data_vt=data.loc[data["Region"]==str_reg]
	#Plot Maximum Temperature
	plt.hist(data_vt["MaxTemp"])
	plt.xlabel("Maximum Temperature (°C)")
	plt.ylabel("Number of observations")
	plt.title("Maximum Temperature Histogram of Victoria")
	plt.show()
	#Plot Rainfall
	plt.hist(data_vt["Rainfall"],range=(0,30))
	plt.xlabel("Rainfall (mm)")
	plt.ylabel("Number of observations")
	plt.title("Rainfall Histogram of Victoria")
	plt.show()
	#Plot Windgustspeed
	plt.hist(data_vt["WindGustSpeed"],range=(0,100))
	plt.xlabel("Strongest Wind Gust (km/h)")
	plt.ylabel("Number of observations")
	plt.title("Strongest Wind Gust Histogram of Victoria")
	plt.show()
	#Plot humidity
	plt.hist(data_vt["Humidity3pm"])
	plt.xlabel("Humidity at 3pm (%)")
	plt.ylabel("Number of observations")
	plt.title("Humidiity at 3pm Histogram of Victoria")
	plt.show()
	#Plot pressure
	plt.hist(data_vt["Pressure3pm"])
	plt.xlabel("Pressure at 3pm (atm)")
	plt.ylabel("Number of observations")
	plt.title("Pressure at 3pm Histogram of Victoria")
	plt.show()