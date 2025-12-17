"""
It is a Cross Platform Library for creating 2D Plots and Graphs from Data in Python
It is a an open source python library used for data visualization and plotting.
visulization like line plots, scatter plots, bar charts, histograms, and more.

Core Plotting Functions
plt.plot(x, y)
Creates line plots - the most basic and commonly used function for visualizing data trends.

python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
Creates scatter plots to visualize relationships between two variables using dots.

python
plt.scatter(x, y, color='red')
plt.show()
plt.bar(x, height)
Creates bar charts - excellent for comparing categories.

python
categories = ['A', 'B', 'C']
values = [3, 7, 5]
plt.bar(categories, values)
plt.show()
plt.hist(data)
Creates histograms to visualize the distribution of data.

python
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5)
plt.show()
plt.pie(values, labels)
Creates pie charts to represent proportions of categories.

python
sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(sizes, labels=labels)
plt.show()
Customization Functions
plt.title()
Adds a title to your plot for clarity.

python
plt.title('Sales Data 2024')
plt.xlabel() and plt.ylabel()
Label your axes for better context and readability.

python
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.legend()
Helps distinguish multiple plotted lines or data series.

python
plt.plot(x, y1, label='Product A')
plt.plot(x, y2, label='Product B')
plt.legend()
plt.grid()
Adds a grid to your plot - improves visual structure and accuracy.

python
plt.grid(True)
Layout & Display Functions
plt.figure(figsize=(width, height))
Customizes the size of your graph.

python
plt.figure(figsize=(10, 6))
plt.subplot(rows, cols, index)
Creates multiple plots in one figure - useful for dashboards.

python
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y1)
plt.subplot(1, 2, 2)  # 2nd plot
plt.plot(x, y2)
plt.subplots(nrows, ncols)
Creates a figure with multiple subplots at once (more flexible than subplot).

python
fig, axs = plt.subplots(2, 2)  # 2x2 grid
axs[0, 0].plot(x, y)
plt.show()
Displays the plot - must be called at the end to render the visualization.

python
plt.show()

"""