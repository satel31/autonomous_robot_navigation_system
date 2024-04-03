import matplotlib.pyplot as plt
from src.map import Map


def visualize(map: Map, path: list, opt_path: list, start: tuple, goal: tuple):
    """
    Visualizes the path on the map
    """
    # Makes map
    plt.imshow(map.grid, cmap='Greys', origin='lower', extent=[0, map.width, 0, map.height], aspect='equal')
    plt.xticks(range(map.width))
    plt.yticks(range(map.height))
    plt.grid(color='k', linestyle='-', linewidth=1)

    # Adds point on the map
    plt.plot(start[0], start[1], 'ro')
    plt.plot(goal[0], goal[1], 'go')

    # Adds paths on the map
    for i in range(len(path) - 1):
        plt.plot([path[i][0], path[i + 1][0]], [path[i][1], path[i + 1][1]], 'b-')

    for i in range(len(opt_path) - 1):
        plt.plot([opt_path[i][0], opt_path[i + 1][0]], [opt_path[i][1], opt_path[i + 1][1]], 'm-')

    plt.show()
