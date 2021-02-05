# Generates a plot of cubes with scatter() using a colormap for flair and save it
import matplotlib.pyplot as plt

x_values = range(1, 101)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=10)

# Set chart title and lable axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)


# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set Axis range 
ax.axis([0, 100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')



