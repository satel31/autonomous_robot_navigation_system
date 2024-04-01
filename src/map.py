from random import randint


class Map:
    def __init__(self, min_width: int = 0, min_height: int = 0, max_width: int = 10, max_height: int = 10) -> None:
        """Makes a grid with random amount of cells. Min - 0, default max - 100"""
        self.width = randint(min_width, max_width)
        self.height = randint(min_height, max_height)

        # Make grid of zeros
        self.grid = [[0] * self.width for _ in range(self.height)]

        # Random count of obstacles from 0 to max count of cells on the map
        obstacles_count = randint(0, self.width * self.height)

        for _ in range(obstacles_count):
            # Choose random coordinates for cell
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)

            # Make this random cell an obstacle. 0 means free, 1 means obstacle
            self.grid[y][x] = 1

    def is_obstacle(self, x: int, y: int) -> bool:
        """Check if the cell is an obstacle"""
        return self.grid[y][x] == 1

    def __str__(self) -> str:
        grid_str = ""
        for row in self.grid:
            grid_str += "".join(str(cell) for cell in row) + "\n"
        return grid_str
