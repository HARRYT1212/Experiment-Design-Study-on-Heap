# Zechen Tian 1723669
# I implemented this file independently for assignment.

import time
from generator import(
    generate_push_sequence,
    generate_push_getTop_sequence,
    generate_push_pop_sequence
)
from MaxHeap import MaxHeap
from Competitor import CompetitorArray
import matplotlib.pyplot as plt
import random

def run_sequence(ds, sequence):
  start_time = time.perf_counter()
  for op in sequence:
        if op[0] == 1:
            ds.push(op[1])
        elif op[0] == 2:
            ds.pop()
        else:
            ds.getTop()
  end_time = time.perf_counter()
  return end_time - start_time

# Experiment 3
def experiment_3():
  M = 10**6
  L = M
  percentage = [0.001, 0.005, 0.01, 0.05, 0.1]
  seeds_3 = [301, 302, 303, 304, 305]

  heap = MaxHeap()
  array = CompetitorArray()

  heap_time = []
  array_time = []

  for pct, seed in zip(percentage, seeds_3):
    random.seed(seed) # set the random seed
    
    print(f"Running Exp 3 for pct = {pct}")
    seq = generate_push_pop_sequence(L, pct)

    heap.reset()
    t_heap = run_sequence(heap, seq)
    heap_time.append(t_heap)

    array.reset()
    t_array = run_sequence(array, seq)
    array_time.append(t_array)

    print(f"Heap: {heap_time[-1]:.4f}s")
    print(f"Array: {array_time[-1]:.4f}s")

  return [p * 100 for p in percentage], heap_time, array_time

def plot_experiment(x, y1, y2, label1, label2, xlabel, ylabel, title, filename):
    plt.figure(figsize=(8, 6))

    plt.plot(x, y1, marker='o', label=label1)
    plt.plot(x, y2, marker='s', label=label2)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)

    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()

def main():
    x3, heap3, array3 = experiment_3()
    plot_experiment(
        x3,
        heap3,
        array3,
        "Max-Heap",
        "Array",
        "pop Percentage (%)",
        "Running Time (seconds)",
        "Exp 3: Time vs pop Percentage",
        "exp3_pop_percentage.png"
    )
if __name__ == "__main__":
    main()    