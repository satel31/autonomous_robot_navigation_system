import matplotlib.pyplot as plt


def visualize(map, path, opt_path, start, goal):
    plt.imshow(map.grid, cmap='Greys', origin='lower', extent=[0, map.width, 0, map.height], aspect='equal')

    plt.plot(start[0], start[1], 'ro')
    plt.plot(goal[0], goal[1], 'go')

    for i in range(len(path) - 1):
        plt.plot([path[i][0], path[i + 1][0]], [path[i][1], path[i + 1][1]], 'b-')

    for i in range(len(opt_path) - 1):
        plt.plot([opt_path[i][0], opt_path[i + 1][0]], [opt_path[i][1], opt_path[i + 1][1]], 'm-')

    plt.xticks(range(map.width))
    # plt.xlim(0, map.width - 1)

    plt.yticks(range(map.height))
    # plt.gca().invert_yaxis()
    # plt.ylim(0, map.height - 1)
    plt.grid(color='k', linestyle='-', linewidth=1)
    plt.show()
