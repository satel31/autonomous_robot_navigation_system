import pytest
from src.map import Map

@pytest.fixture
def random_map():
    return Map()

@pytest.fixture
def fixed_map():
    return Map(5, 5, 5, 5)

def test_random_map_init(random_map):
    assert 0 <= random_map.width <= 10
    assert 0 <= random_map.height <= 10
    assert len(random_map.grid) == random_map.height

def test_fixed_map_init(fixed_map):
    assert 0 <= fixed_map.width <= 5
    assert 0 <= fixed_map.height <= 5
    assert len(fixed_map.grid) == fixed_map.height
