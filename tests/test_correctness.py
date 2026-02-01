from algorithms.registry import ALGORITHMS
from benchmarks.sorting_inputs import random_array

def test_sorting_algorithms():
    data = random_array(100)
    expected = sorted(data)

    for algo in ALGORITHMS["sorting"].values():
        assert algo(data) == expected
