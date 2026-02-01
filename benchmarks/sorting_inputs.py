import random

def random_array(n: int) -> list[int]:
    return [random.randint(0, n) for _ in range(n)]

def nearly_sorted(n: int) -> list[int]:
    arr = list(range(n))
    for _ in range(n // 10):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def reversed_array(n: int) -> list[int]:
    return list(range(n, 0, -1))
