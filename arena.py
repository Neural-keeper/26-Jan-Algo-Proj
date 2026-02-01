import json
import time
from algorithms.registry import ALGORITHMS
from benchmarks.sorting_inputs import random_array

RESULTS_FILE = "results/runs.jsonl"

def benchmark(problem, input_data):
    baseline = sorted(input_data)

    for name, algo in ALGORITHMS[problem].items():
        start = time.perf_counter()
        output = algo(input_data)
        duration = time.perf_counter() - start

        correct = output == baseline

        record = {
            "problem": problem,
            "algorithm": name,
            "n": len(input_data),
            "time": duration,
            "correct": correct,
        }

        with open(RESULTS_FILE, "a") as f:
            f.write(json.dumps(record) + "\n")
            

if __name__ == "__main__":
    data = random_array(5_000)
    benchmark("sorting", data)
