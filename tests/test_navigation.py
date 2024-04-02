import pytest
from src.navigation import astar_algorithm


@pytest.fixture
def grid_no_way():
    return [[0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0]]


@pytest.fixture
def grid_way():
    return [[0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0, 1], [1, 1, 0, 0]]


def test_navigation_no_way(grid_no_way):
    assert astar_algorithm(grid_no_way, (0, 0), (3, 2)) == "До этой точки нет пути"


def test_navigation_way(grid_way):
    assert astar_algorithm(grid_way, (0, 0), (3, 3)) == [(0, 0), (1, 1), (2, 2), (3, 3)]
