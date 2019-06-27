import matplotlib.pyplot as plt
from fill_walk import random_walk

while True:
    rw = random_walk.RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, s=15,
                c=point_numbers,cmap=plt.cm.Blues,edgecolor='none')
    plt.scatter(0,0,c='green',edgecolors='none',s=90)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolors='none',s=90)
    # #隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    #plt.figure(figsize=(10,6))
    plt.title('Random Walk', fontsize=14)
    plt.xlabel('Value', fontsize=10)
    plt.ylabel('y_value', fontsize=10)
    plt.show()
    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break
