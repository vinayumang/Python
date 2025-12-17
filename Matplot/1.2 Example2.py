# Load the Product.csv in which product name defined as x-axis and 
# product total price defined as y-axis and plot a graph using matplotlib.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Excel/Product.csv")
plt.plot(df["Name"], df["Total_Price"])
plt.title("Product Total Price")
plt.xlabel("Product Name")
plt.ylabel("Total Price")
plt.show()
plt.legend() # Optional: Add legend to the graph
plt.savefig("Product_Total_Price_Graph.png")


#More simple Way
# df = pd.read_csv("Excel/Product.csv")
# x=df["Name"]
# y=df["Total_Price"]
# plt.plot(x, y)
# plt.title("Product Total Price")
# plt.xlabel("Product Name")
# plt.ylabel("Total Price")
# plt.show()
# plt.legend() # Optional: Add legend to the graph
# plt.savefig("Product_Total_Price_Graph.png")