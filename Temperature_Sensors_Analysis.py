# ==========================================
# PART 1: Temperature Sensor Data Analysis
# ==========================================
#---1.1---
import numpy as np

data = np.genfromtxt('Sensors_data.csv', delimiter=',')

print("Shape : ",data.shape)
print("Data type : ",data.dtype)
#30 days , 6 sensors
print("____________________________________________________________________")
#---1.2---
mask = (data == -999)
print ("sum_of_broken_sensors : ", np.sum(mask))
print ("For every sensor : ",np.sum(mask,axis=0))
print("____________________________________________________________________")
#---1.3---
cleaned_data = data.copy()
cleaned_data[cleaned_data == -999] = np.nan 
NaN_count = np.sum(np.isnan(cleaned_data))
print("number of nan : ",NaN_count)
print("____________________________________________________________________")
#---1.4---
Broken_sensor = np.argmax(np.sum(mask,axis=0))
max_broken_count = np.max(np.sum(mask,axis=0))
print ("index of the broken sensor : ",Broken_sensor)
print ("number of broken readings : ",max_broken_count)
print("percentage of readings : ",(max_broken_count/30)*100,"%")
print("____________________________________________________________________")
#---1.5---
means = np.nanmean(cleaned_data,axis=0)
imputed_data = np.where(data==-999,means,data)
print(imputed_data)
print("____________________________________________________________________")
#---1.6---
final_means = np.mean(imputed_data,axis=0)
final_std = np.std(imputed_data,axis=0)
print("means for each sensor : ",final_means)
print("std for each sensor : ",final_std)
