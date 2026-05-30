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

# Experiment 2
def experiment_2(repeats=5):
  M = 10**6
  L = M
  percentage = [0.001, 0.005, 0.01, 0.05, 0.1]

  heap = MaxHeap()
  array = CompetitorArray()

  heap_time = []
  array_time = []

  for pct in percentage:
    print(f"Running Exp 2 for pct = {pct}")

    heap_runs = []
    array_runs = []

    # Repeat the experiment and take the average
    for r in range(repeats):
      seed = 2000 + int(pct * 1000000) + r
      random.seed(seed) # Set the random seed

      seq = generate_push_getTop_sequence(L, pct)

      heap.reset()
      t_heap = run_sequence(heap, seq)
      heap_runs.append(t_heap)

      array.reset()
      t_array = run_sequence(array, seq)
      array_runs.append(t_array)

      print(f"  Repeat {r+1}: Heap = {t_heap:.4f}s, Array = {t_array:.4f}s")

    avg_heap = sum(heap_runs) / repeats
    avg_array = sum(array_runs) / repeats

    heap_time.append(avg_heap)
    array_time.append(avg_array)

    print(f"Average Heap: {avg_heap:.4f}s")
    print(f"Average Array: {avg_array:.4f}s")

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
    x2, heap2, array2 = experiment_2()
    plot_experiment(
        x2,
        heap2,
        array2,
        "Max-Heap",
        "Array",
        "getTop Percentage (%)",
        "Running Time (seconds)",
        "Exp 2: Time vs getTop Percentage",
        "exp2_gettop_percentage.png"
    )
if __name__ == "__main__":
    main()