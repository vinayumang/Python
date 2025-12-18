#Attributes for plot()
# color: specifies the color of the line
# linestyle: specifies the style of the line
# linewidth: specifies the width of the line
# marker: specifies the marker style
# markersize: specifies the size of the marker
# label: specifies a label for the legend
# alpha: specifies transparency (0-1)
# drawstyle: specifies how to draw lines between points

#Syntax:plt.plot(x, y, color='blue', linestyle='-',
#  linewidth=2, marker='o', markersize=6, label='Data', alpha=0.8, drawstyle='default')

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('Excel/Sale.csv')
plt.plot(df['Week1'], df['Week2'],df['Week3'])
plt.title("Sale of 3 week line graph")
plt.xlabel("Day number of week")
plt.ylabel("Sale amount of day")
plt.plot(kind='line', color='green', linestyle='--',linewidth=2, marker='o', markersize=8, label='Sale Data', alpha=0.7, drawstyle='default')
plt.show()  