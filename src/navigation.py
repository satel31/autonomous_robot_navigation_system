from heapq import heappush, heappop


def way_cost(current, goal):
    """
       Эвристическая функция для оценки расстояния от текущей точки до цели.
       Здесь используется диагональное расстояние (можно двигаться по вертикали, горизонтали и диагонали).

       :param current: Текущая точка в формате (x, y).
       :param goal: Целевая точка в формате (x, y).
       :return: Оценка расстояния от текущей точки до цели.
       """
    x = abs(current[0] - goal[0])
    y = abs(current[1] - goal[1])
    return max(x, y)


def astar_algorithm(grid, start, goal):
    """
       Реализация алгоритма A* для нахождения кратчайшего пути от start до goal на карте grid.

       :param grid: Карта пространства с препятствиями, представленная двумерным списком, где 0 - свободная ячейка,
                    1 - препятствие.
       :param start: Координаты начальной точки в формате (x, y).
       :param goal: Координаты конечной точки в формате (x, y).
       :return: Кратчайший путь от start до goal в виде списка координат точек.
    """
    # List for open (not checked) points
    open_list = []
    # Set with closed (checked) points
    closed = ()
    # Parents points (key -> current point, def -> previous point)
    parents = {}
    # Cost from start to current point
    cost = {start: 0}

    total_cost = way_cost(start, goal)
    # Makes heap from list and put tuple there in order from min to max by total_cost
    heappush(open_list, (total_cost, start))

    while open_list:
        _, current_point = heappop(open_list)

        if current_point == goal:
            path = []
            while current_point:
                path.append(current_point)
                current_point = parents.get(current_point)
            return path[::-1]
