import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter (rw.x_values, rw.y_values, s =15)
    point_numbers = list(range(rw.num_points))
    plt.scatter (rw.x_values,rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors= 'none', s = 15)
    plt.show()

    keep_runing = input ("Make anothe walk? (y/n):")
    if keep_runing == 'n':
        break