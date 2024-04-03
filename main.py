from src.map import Map
from src.navigation import astar_algorithm, optimization
from src.visualization import visualize

map = Map()
print(map)

# for test
start = (0, 0)
goal = (2, 3)

if len(map.grid) == 0:
    print("Сгенерировалась пустая карта")
elif map.height <= goal[1] or map.width <= goal[0]:
    print("Точка цели вне карты")
else:
    if map.is_obstacle(*start):
        print("Начало является препятствием")
    elif map.is_obstacle(*goal):
        print("Цель является препятствием")
    else:
        path = astar_algorithm(map.grid, start, goal)
        print(path)
        if type(path) != str:
            opt_path = optimization(path, map.grid)
            print(opt_path)
            visualize(map, path, opt_path, start, goal)
