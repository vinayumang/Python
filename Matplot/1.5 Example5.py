#10 students height and weight data draw a graph (line,bar,barh)

import matplotlib.pyplot as plt 
import pandas as pd
df=pd.read_csv('Excel/Student.csv')
height=df['Height(cm)']
weight=df['Weight(kg)']
plt.plot(height,weight,marker='o') #line graph
plt.title('Height vs Weight')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()

plt.bar(height,weight) #bar graph
plt.title('Height vs Weight')
plt.xlabel('Height')
plt.ylabel('Weight')    
plt.show()

plt.barh(height,weight) #horizontal bar graph
plt.title('Height vs Weight')
plt.xlabel('Weight')
plt.ylabel('Height')    
plt.show()