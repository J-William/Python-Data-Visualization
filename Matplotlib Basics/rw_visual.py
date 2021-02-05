# Creates a visually appealing random walk with first and last
# points denoted and a color gradient denoting progression 
import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
	rw = RandomWalk(50000)
	rw.fill_walk()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(20,16), dpi=92)
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Wistia, edgecolors='none', s=3)
	ax.scatter(0,0, c='green', edgecolors='none', s=10)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=12)

	# Remove the axes to improve visuals
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break

