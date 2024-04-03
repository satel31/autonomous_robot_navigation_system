from heapq import heappush, heappop


def way_cost(current: tuple, goal: tuple) -> int:
    """
    Asses destination from current point to the goal.
    """
    x = abs(current[0] - goal[0])
    y = abs(current[1] - goal[1])
    return max(x, y)


def get_neighbors(grid: list, current_point: tuple) -> list:
    """
    Get neighbors of current point on the map
    """
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        x = current_point[0] + dx
        y = current_point[1] + dy
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == 0:
            neighbors.append((x, y))
    return neighbors


def is_valid_line(start: tuple, end: tuple, grid: list) -> bool:
    """
    Check if there are obstacles in the way
    """
    x0, y0 = start
    x1, y1 = end

    # Direct line from start to end
    line_points = [(x, y) for x in range(min(x0, x1), max(x0, x1) + 1)
                   for y in range(min(y0, y1), max(y0, y1) + 1)]

    # Check obstacles
    for point in line_points:
        x, y = point
        if grid[y][x] == 1:
            return False

    return True


def optimization(path: list, grid: list) -> list:
    """
    Optimizes the path
    """
    smoothed_path = [path[0]]

    for i in range(1, len(path) - 1):
        # Check if we can connect current and next point
        if is_valid_line(path[i - 1], path[i + 1], grid):
            continue
        else:
            smoothed_path.append(path[i])
    smoothed_path.append(path[-1])

    return smoothed_path


def astar_algorithm(grid: list, start: tuple, goal: tuple) -> list | str:
    """
    A* algorithm for finding the shortest path from start to goal on a grid
    """
    # List for open (not checked) points
    open_list = []
    # Set with closed (checked) points
    closed = set()
    # Parents points (key -> current point, value -> previous point)
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
            # The best way
            return path[::-1]

        closed.add(current_point)

        for neighbor in get_neighbors(grid, current_point):
            if neighbor in closed:
                continue
            tent_cost = cost[current_point] + 1

            if neighbor not in [i[1] for i in open_list]:
                heappush(open_list, (tent_cost + way_cost(neighbor, goal), neighbor))
            elif tent_cost >= cost.get(neighbor):
                # Not the best way
                continue
            parents[neighbor] = current_point
            cost[neighbor] = tent_cost
    # There is no way
    return "До этой точки нет пути"
