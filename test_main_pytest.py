import pytest
from main import calculate_average

def test_positive_numbers():
    assert calculate_average([1, 2, 3]) == 2
    assert calculate_average([4, 5, 6, 7]) == 6

def test_negative_numbers():
    assert calculate_average([-3, -3, -3]) == -3
    assert calculate_average([-2, -4, -6]) == -4

def test_mixed_numbers():
    assert calculate_average([10, -10]) == 0
    assert calculate_average([0, 0, 1]) == 0

def test_empty_list():
    assert calculate_average([]) is None
