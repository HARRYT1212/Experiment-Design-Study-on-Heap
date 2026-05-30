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

# Experiment 1
def experiment_1():
  M = 10**6
  length = [int(0.1*M), int(0.2*M), int(0.5*M), int(0.8*M), int(1*M)]

  heap = MaxHeap()
  array = CompetitorArray()

  heap_time = []
  array_time = []

  for L in length:
    print(f"Running Exp 1 for L = {L}")
    seq = generate_push_sequence(L)

    heap.reset()
    t_heap = run_sequence(heap, seq)
    heap_time.append(t_heap)

    array.reset()
    t_array = run_sequence(array, seq)
    array_time.append(t_array)

    print(f"Heap: {heap_time[-1]:.4f}s")
    print(f"Array: {array_time[-1]:.4f}s")

  return length, heap_time, array_time

# define the plot function
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
    random.seed(1300)
    # Plot 1: Time vs. Length of push only sequence
    x1, heap1, array1 = experiment_1()
    plot_experiment(
        x1,
        heap1,
        array1,
        "Max-Heap",
        "Array",
        "Sequence Length L",
        "Running Time (seconds)",
        "Exp 1: Time vs Length of Push-Only Sequence",
        "exp1_push.png"
    )

if __name__ == "__main__":
   main()