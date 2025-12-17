#Graph of Day and Temperature

import matplotlib.pyplot as plt 
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temp=[22,24,21,23,25,26,27]
plt.plot(days, temp)
plt.title("Temperature Graph")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()