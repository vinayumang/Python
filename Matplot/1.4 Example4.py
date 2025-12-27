#Bar graph

import matplotlib.pyplot as plt
import pandas as pd 
df=pd.read_csv('Excel/Sale.csv')
df.plot(kind='bar', x='Days', y=['Week1', 'Week2', 'Week3'], color=['blue', 'orange', 'green'])
plt.title("Sale of 3 week bar graph")
plt.xlabel("Day number of week")
plt.ylabel("Sale amount of day")
plt.show()  


#plt.bar(df['Days'], df['Week1'], color='blue', label='Week1')
#plt.bar(df['Days'], df['Week2'], bottom=df['Week1'], color='orange', label='Week2')
#plt.bar(df['Days'], df['Week3'], bottom=df['Week1']+df['Week2'], color='green', label='Week3