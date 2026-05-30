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

# Push by heapify operation
def build_heap_Heapify(sequence):
  keys = [op[1] for op in sequence if op[0] == 1]
  heap = MaxHeap()
  start_time = time.perf_counter()
  heap.heapify(keys)
  end_time = time.perf_counter()
  return end_time - start_time

# Push-one-by-one operation
def build_heap_Push(sequence):
  heap = MaxHeap()
  start_time = time.perf_counter()
  for op in sequence:
    if op[0] == 1:
      heap.push(op[1])
  end_time = time.perf_counter()
  return end_time - start_time

# Experiment 4
def experiment_4(repeats=5):
  M = 10**6
  length = [int(0.1*M), int(0.2*M), int(0.5*M), int(0.8*M), int(1*M)]

  Heapify_times = []
  Push_times = []

  for L in length:
    print(f"Running Exp 4 for L = {L}")

    heapify_runs = []
    push_runs = []

    # repeat the experiment and take the average, repeat 5 times
    for r in range(repeats):
      seed = 4000 + L + r
      random.seed(seed) # set the random seed

      seq = generate_push_sequence(L)

      Heapify_time = build_heap_Heapify(seq)
      heapify_runs.append(Heapify_time)

      Push_time = build_heap_Push(seq)
      push_runs.append(Push_time)

      print(f"  Repeat {r+1}: Heapify = {Heapify_time:.4f}s, Push-one-by-one = {Push_time:.4f}s")

    avg_heapify = sum(heapify_runs) / repeats
    avg_push = sum(push_runs) / repeats

    Heapify_times.append(avg_heapify)
    Push_times.append(avg_push)

    print(f"Average Heapify time: {avg_heapify:.4f}s")
    print(f"Average Push-one-by-one time: {avg_push:.4f}s")

  return length, Heapify_times, Push_times

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

    x4, heap4, array4 = experiment_4()
    plot_experiment(
        x4,
        heap4,
        array4,
        "Heapify Time (seconds)",
        "Push-one-by-one Time (seconds)",
        "Sequence Length L",
        "Running Time (seconds)",
        "Exp 4: Heapify vs Push-one-by-one",
        "exp4_heapify_push.png"
    )

if __name__ == "__main__":
    main()